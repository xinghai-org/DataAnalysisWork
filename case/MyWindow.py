# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 653)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial Nova")
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-image: url(:/bakground/img/bj.jpg);\n"
"    background-position:center;\n"
"    border-radius:30px;\n"
"    background-color: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 9, 15, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_2.setStyleSheet("background-color: none;")
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toolButton_8 = QtWidgets.QToolButton(self.widget_2)
        self.toolButton_8.setMinimumSize(QtCore.QSize(25, 25))
        self.toolButton_8.setMaximumSize(QtCore.QSize(25, 25))
        self.toolButton_8.setStyleSheet("border-radius:12px;\n"
"background-color: rgba(85, 255, 127, 155);")
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout.addWidget(self.toolButton_8)
        self.toolButton_9 = QtWidgets.QToolButton(self.widget_2)
        self.toolButton_9.setMinimumSize(QtCore.QSize(25, 25))
        self.toolButton_9.setMaximumSize(QtCore.QSize(25, 25))
        self.toolButton_9.setStyleSheet("border-radius:12px;\n"
"background-color: rgba(255, 255, 127, 155);")
        self.toolButton_9.setObjectName("toolButton_9")
        self.horizontalLayout.addWidget(self.toolButton_9)
        self.toolButton_5 = QtWidgets.QToolButton(self.widget_2)
        self.toolButton_5.setMinimumSize(QtCore.QSize(25, 25))
        self.toolButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.toolButton_5.setStyleSheet("border-radius:12px;\n"
"background-color: rgba(255, 0, 0, 155);")
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout.addWidget(self.toolButton_5)
        self.verticalLayout.addWidget(self.widget_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: none;")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(10, 10, 10, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.toolButton = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(230, 130))
        self.toolButton.setMaximumSize(QtCore.QSize(100, 100))
        self.toolButton.setStyleSheet("border-radius:20px;\n"
"background-color: rgba(252, 255, 198, 150);")
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 1, 0, 1, 1)
        self.toolButton_4 = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_4.sizePolicy().hasHeightForWidth())
        self.toolButton_4.setSizePolicy(sizePolicy)
        self.toolButton_4.setMinimumSize(QtCore.QSize(230, 130))
        self.toolButton_4.setMaximumSize(QtCore.QSize(100, 100))
        self.toolButton_4.setStyleSheet("border-radius:20px;\n"
"background-color: rgba(252, 255, 198, 150);")
        self.toolButton_4.setObjectName("toolButton_4")
        self.gridLayout.addWidget(self.toolButton_4, 0, 0, 1, 1)
        self.toolButton_3 = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setMinimumSize(QtCore.QSize(230, 130))
        self.toolButton_3.setMaximumSize(QtCore.QSize(100, 100))
        self.toolButton_3.setMouseTracking(False)
        self.toolButton_3.setTabletTracking(False)
        self.toolButton_3.setStyleSheet("border-radius:20px;\n"
"background-color: rgba(252, 255, 198, 150);")
        self.toolButton_3.setCheckable(False)
        self.toolButton_3.setAutoRepeat(False)
        self.toolButton_3.setAutoExclusive(False)
        self.toolButton_3.setAutoRaise(False)
        self.toolButton_3.setObjectName("toolButton_3")
        self.gridLayout.addWidget(self.toolButton_3, 0, 2, 1, 1)
        self.toolButton_2 = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QtCore.QSize(230, 130))
        self.toolButton_2.setMaximumSize(QtCore.QSize(100, 100))
        self.toolButton_2.setStyleSheet("border-radius:20px;\n"
"background-color: rgba(252, 255, 198, 150);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.gridLayout.addWidget(self.toolButton_2, 0, 1, 1, 1)
        self.toolButton_6 = QtWidgets.QToolButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_6.sizePolicy().hasHeightForWidth())
        self.toolButton_6.setSizePolicy(sizePolicy)
        self.toolButton_6.setMinimumSize(QtCore.QSize(230, 130))
        self.toolButton_6.setMaximumSize(QtCore.QSize(100, 100))
        self.toolButton_6.setStyleSheet("border-radius:20px;\n"
"background-color: rgba(252, 255, 198, 150);")
        self.toolButton_6.setObjectName("toolButton_6")
        self.gridLayout.addWidget(self.toolButton_6, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolButton_5.clicked.connect(MainWindow.close) # type: ignore
        self.toolButton_8.clicked.connect(MainWindow.showMinimized) # type: ignore
        self.toolButton_9.clicked.connect(MainWindow.showMaximized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_8.setText(_translate("MainWindow", "-"))
        self.toolButton_9.setText(_translate("MainWindow", "◱"))
        self.toolButton_5.setText(_translate("MainWindow", "×"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">员工离职情况分析</span></p></body></html>"))
        self.toolButton.setText(_translate("MainWindow", "离职人数工龄分布"))
        self.toolButton_4.setText(_translate("MainWindow", "离职员工工资情况"))
        self.toolButton_3.setText(_translate("MainWindow", "工资等级与工资数量关系"))
        self.toolButton_2.setText(_translate("MainWindow", "工资与各项统计"))
        self.toolButton_6.setText(_translate("MainWindow", "离职预测"))
import MyWindow_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
