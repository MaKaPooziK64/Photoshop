from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QListWidget , QHBoxLayout, QVBoxLayout, QLabel,QFileDialog)
import os


app = QApplication([])
win = QWidget()
win.setWindowTitle('Easy Editor')
win.resize(700,460)
text = QLabel('Картинка')
list_label = QListWidget()

paintbrush_button = QPushButton('Кисть')
scale_button = QPushButton('Масштаб')
btn_dir = QPushButton('Папка')
left_button = QPushButton('Лево')
right_button = QPushButton('Право')
mirror_button = QPushButton('Зеркало')
blur_button = QPushButton('Резкость')
blackwhite_button = QPushButton('Ч/Б')

h_line = QHBoxLayout() #Основная строка
v_line = QVBoxLayout() #Делим на два столбика
v_line2 = QVBoxLayout() #Делим на два столбика
v_line.addWidget(btn_dir) 
v_line.addWidget(list_label)
v_line2.addWidget(text,95)
h_line_tools = QHBoxLayout()
h_line_tools.addWidget(btn_dir)
h_line_tools.addWidget(left_button)
h_line_tools.addWidget(right_button)
h_line_tools.addWidget(mirror_button)
h_line_tools.addWidget(blur_button)
h_line_tools.addWidget(blackwhite_button)
v_line2.addLayout(h_line_tools)
h_line.addLayout(v_line,20)
h_line.addLayout(v_line2,80)

win.setLayout(h_line)
win.show()
app.exec()