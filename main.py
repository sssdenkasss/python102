from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog,
    QLabel, QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

app = QApplication([])
win = QWidget()
win.resize(1200, 700)
win.setWindowTitle('Easy Editor')
win.setStyleSheet('background-color:#90EE90; font-size:24px; padding: 5px; color:White')

lb_image = QLabel('Картинка')
btn_dir = QPushButton('Папка')
lw_files = QListWidget()
btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_flip = QPushButton('Віддзеркалити')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('Ч-б')

btn_dir.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')

btn_left.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_right.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_flip.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_sharp.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')
btn_bw.setStyleSheet('background-color:blue; border:2px solid white; border-radius: 10px')

row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()
col3 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)
col2.addWidget(lb_image)
col3.addWidget(btn_left)
col3.addWidget(btn_right)
col3.addWidget(btn_flip)
col3.addWidget(btn_sharp)
col3.addWidget(btn_bw)

row.addLayout(col1, 20)
row.addLayout(col2, 60)
row.addLayout(col3, 20)
win.setLayout(row)

win.show()
app.exec_()
