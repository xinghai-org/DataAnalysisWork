# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 390)
        MainWindow.setMinimumSize(QtCore.QSize(695, 390))
        MainWindow.setMaximumSize(QtCore.QSize(710, 695))
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 321))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\./img/背景图.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.btn_1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\./img/图标-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_1.setIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\./img/图标-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_2.setIcon(icon1)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\./img/图标-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_3.setIcon(icon2)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\./img/图标-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_4.setIcon(icon3)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\./img/图标-5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_5.setIcon(icon4)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_4)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_5)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.btn_1.setText(_translate("MainWindow", "各区二手房均价分析"))
        self.btn_1.setToolTip(_translate("MainWindow", "各区二手房均价分析"))
        self.btn_2.setText(_translate("MainWindow", "各区二手房数量所占比例"))
        self.btn_2.setToolTip(_translate("MainWindow", "各区二手房数量所占比例"))
        self.btn_3.setText(_translate("MainWindow", "全市二手房装修程度分析"))
        self.btn_3.setToolTip(_translate("MainWindow", "全市二手房装修程度分析"))
        self.btn_4.setText(_translate("MainWindow", "热门户型均价分析"))
        self.btn_4.setToolTip(_translate("MainWindow", "热门户型均价分析"))
        self.btn_5.setText(_translate("MainWindow", "二手房售价预测"))
        self.btn_5.setToolTip(_translate("MainWindow", "二手房售价预测"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
