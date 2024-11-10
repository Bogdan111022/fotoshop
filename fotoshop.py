import os
from PIL import Image, ImageFilter
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QFileDialog,
    QLabel,QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

class PhotoManager:
    def __init__(self):
        self.photo = None
        self.folder = None
        self.filename = None
        self.image_lbl = None

    def load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.photo = Image.open(image_path)
    
    def show_image(self, image_lbl):
        pixels = pil2pixmap(self.photo)
        pixels = pixels.scaledToWidth(500)
        image_lbl.setPixmap(pixels)

    def bw(self):
        self.photo = self.photo.convert("L")
        self.show_image(self.image_lbl)
    

    def left(self):
        self.photo = self.photo.transpose(Image.ROTATE_90)
        self.show_image(self.image_lbl)

    def flip(self):
        self.photo = self.photo.transpose(Image.FLIP_LEFT_RIGHT)
        self.show_image(self.image_lbl)

    def sharp(self):
        self.photo = self.photo.filter(ImageFilter.SHARPEN)
        self.show_image(self.image_lbl)

    def pressing(self):
        self.photo = self.photo.filter(ImageFilter.EMBOSS )
        self.show_image(self.image_lbl)

    def smoothing(self):
        self.photo = self.photo.filter(ImageFilter.SMOOTH   )
        self.show_image(self.image_lbl)


    def right(self):
        self.photo = self.photo.transpose(Image.ROTATE_270)
        self.show_image(self.image_lbl)

    def contours(self):
        self.photo = self.photo.filter(ImageFilter.CONTOUR)
        self.show_image(self.image_lbl)





app = QApplication([])
win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')

lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_filles = QListWidget()

btn_left = QPushButton("Вліво")
btn_right = QPushButton("Вправо")
btn_flip = QPushButton("Відзеркалити")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")
btn_pressing = QPushButton("Тиснення")
btn_smoothing = QPushButton("Згладжування")
btn_contours = QPushButton("Накладення контурів")
row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col1.addWidget(btn_dir)
col1.addWidget(lw_filles)
col2.addWidget(lb_image, 95)

row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_pressing)
row_tools.addWidget(btn_smoothing)
row_tools.addWidget(btn_contours)
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)

photo_manager = PhotoManager()
photo_manager.image_lbl = lb_image


win.show()

photo_manager = PhotoManager()
photo_manager.image_lbl = lb_image

def open_folder():
    photo_manager.folder = QFileDialog.getExistingDirectory()
    files = os.listdir(photo_manager.folder)
    lw_filles.clear()
    lw_filles.addItems(files)
    
    
def show_chosen_image():
    photo_manager.filename = lw_filles.currentItem().text()
    photo_manager.load()
    photo_manager.show_image(lb_image)

lw_filles.currentRowChanged.connect(show_chosen_image)
btn_bw.clicked.connect(photo_manager.bw)
btn_left.clicked.connect(photo_manager.left)
btn_right.clicked.connect(photo_manager.right)
btn_flip.clicked.connect(photo_manager.flip)
btn_sharp.clicked.connect(photo_manager.sharp)
btn_pressing.clicked.connect(photo_manager.pressing)
btn_smoothing.clicked.connect(photo_manager.smoothing)
btn_contours.clicked.connect(photo_manager.contours)

btn_dir.clicked.connect(open_folder)

app.setStyleSheet("""
        QWidget {
            background: #0000ff;
        }


        QPushButton
        {
            background-color: #ffbf00;
            border-style: outset;
            font-family: Roboto;
            max-width: 6em;
            padding: 6px;
            font-size: 20px;
        }

""")











app.exec_()