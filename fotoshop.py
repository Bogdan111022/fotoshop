import os
from PyQt5.QtWidgets import(
    QApplication, QWidget,
    QFileDialog,
    QLabel,QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)

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
col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)
win.setLayout(row)


win.show()

workdir = ''
def filter(files, extensions):
    result = []
    for filename in files:
        for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
    return result

def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()

def showFilesList():
   extensions = ['.jpg', 'jpeg', '.png', '.gif', '.bpm']
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions )

   lw_filles.clear()
   for filename in filenames : 
       lw_filles.addItem(filenames)

btn_dir.clicked.connect(showFilesList)

app.setStyleSheet("""
        QWidget {
            background: #0000ff;
        }


        QPushButton
        {
            background-color: #ffbf00;
            border-style: outset;
            font-family: Roboto;
            main-widht: 6em;
            padding: 6px;
            font-size: 25px;
        }

""")











app.exec_()