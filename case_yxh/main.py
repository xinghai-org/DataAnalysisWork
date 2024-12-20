from MyWindow import *
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtCore import Qt,QPoint
from analysis import DataAnalysis
class MyWindow(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)       #去除边框
        # 记录鼠标按下的初始位置
        
        self.offset = QPoint()
        # 绑定函数
        self.function = DataAnalysis()
        self.to_connect(self.function)
        
    def closeEvent(self, event):
        sys.exit()
    
    def to_connect(self,f):
        self.toolButton_4.clicked.connect(f.gongzi_lzl)
        self.toolButton_2.clicked.connect(f.yxgz)
        self.toolButton_3.clicked.connect(f.gcsl)
        self.toolButton.clicked.connect(f.gongl)
        self.toolButton_6.clicked.connect(f.sjsl)

    def mousePressEvent(self, event):
        # 记录鼠标按下的初始位置
        self.offset = event.pos()
    def mouseMoveEvent(self, event):
        # 移动窗口位置
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)


if __name__ == '__main__':
    app = QApplication([])
    win = MyWindow()
    win.show()
    app.exec()