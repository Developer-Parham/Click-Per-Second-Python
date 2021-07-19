from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
# Parham
# 8 hour and 30 minute project
# github: https://github.com/Developer-Parham/Click-Per-Second-Python.git

class Ui_list_window(object):
    def setupUi(self, list_window):
        list_window.setObjectName("list_window")
        list_window.resize(300, 500)
        list_window.setMinimumSize(QtCore.QSize(300, 500))
        list_window.setMaximumSize(QtCore.QSize(300, 500))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(16)
        list_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("click_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        list_window.setWindowIcon(icon)
        list_window.setStyleSheet("color: black;\n"
                                  "background-color: white;")
        self.centralwidget = QtWidgets.QWidget(list_window)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, -30, 301, 531))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.click_to_start_button = QtWidgets.QPushButton(self.page_2, clicked=lambda: self.Start())
        self.click_to_start_button.setGeometry(QtCore.QRect(50, 200, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(12)
        self.click_to_start_button.setFont(font)
        self.click_to_start_button.setStyleSheet("background-color: #E6E6E6;\n"
                                                 "border: false;\n"
                                                 "border-radius: 20px")
        self.click_to_start_button.setObjectName("click_to_start_button")
        self.cps_label = QtWidgets.QLabel(self.page_2)
        self.cps_label.setGeometry(QtCore.QRect(0, 150, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(30)
        self.cps_label.setFont(font)
        self.cps_label.setStyleSheet("background-color: transparent;")
        self.cps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cps_label.setObjectName("cps_label")
        self.stackedWidget.addWidget(self.page_2)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.s3 = QtWidgets.QPushButton(self.page, clicked=lambda: self.S3_list())
        self.s3.setGeometry(QtCore.QRect(70, 210, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        self.s3.setFont(font)
        self.s3.setStyleSheet("background-color: transparent;\n"
                              "border: false")
        self.s3.setObjectName("s3")
        self.s1 = QtWidgets.QPushButton(self.page, clicked=lambda: self.S1_list())
        self.s1.setGeometry(QtCore.QRect(70, 160, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        self.s1.setFont(font)
        self.s1.setStyleSheet("background-color: transparent;\n"
                              "border: false")
        self.s1.setObjectName("s1")
        self.s10 = QtWidgets.QPushButton(self.page, clicked=lambda: self.S10_list())
        self.s10.setGeometry(QtCore.QRect(70, 310, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        self.s10.setFont(font)
        self.s10.setStyleSheet("background-color: transparent;\n"
                               "border: false")
        self.s10.setObjectName("s10")
        self.s60 = QtWidgets.QPushButton(self.page, clicked=lambda: self.S60_list())
        self.s60.setGeometry(QtCore.QRect(70, 410, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        self.s60.setFont(font)
        self.s60.setStyleSheet("background-color: transparent;\n"
                               "border: false")
        self.s60.setObjectName("s60")
        self.s5 = QtWidgets.QPushButton(self.page, clicked=lambda: self.S5_list())
        self.s5.setGeometry(QtCore.QRect(70, 260, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        self.s5.setFont(font)
        self.s5.setStyleSheet("background-color: transparent;\n"
                              "border: false")
        self.s5.setObjectName("s5")
        self.selecmode = QtWidgets.QLabel(self.page)
        self.selecmode.setGeometry(QtCore.QRect(0, 70, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(17)
        self.selecmode.setFont(font)
        self.selecmode.setStyleSheet("background-color: transparent;\n"
                                     "")
        self.selecmode.setAlignment(QtCore.Qt.AlignCenter)
        self.selecmode.setObjectName("selecmode")
        self.s30 = QtWidgets.QPushButton(self.page, clicked=lambda: self.S30_list())
        self.s30.setGeometry(QtCore.QRect(70, 360, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(14)
        self.s30.setFont(font)
        self.s30.setStyleSheet("background-color: transparent;\n"
                               "border: false")
        self.s30.setObjectName("s30")
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.in3 = QtWidgets.QLabel(self.page_4)
        self.in3.setGeometry(QtCore.QRect(0, 190, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(30)
        self.in3.setFont(font)
        self.in3.setStyleSheet("background-color: transparent")
        self.in3.setAlignment(QtCore.Qt.AlignCenter)
        self.in3.setObjectName("in3")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.in2 = QtWidgets.QLabel(self.page_5)
        self.in2.setGeometry(QtCore.QRect(0, 190, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(30)
        self.in2.setFont(font)
        self.in2.setStyleSheet("background-color: transparent")
        self.in2.setAlignment(QtCore.Qt.AlignCenter)
        self.in2.setObjectName("in2")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.in1 = QtWidgets.QLabel(self.page_6)
        self.in1.setGeometry(QtCore.QRect(0, 190, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(30)
        self.in1.setFont(font)
        self.in1.setStyleSheet("background-color: transparent")
        self.in1.setAlignment(QtCore.Qt.AlignCenter)
        self.in1.setObjectName("in1")
        self.stackedWidget.addWidget(self.page_6)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.sgame = QtWidgets.QLabel(self.page_3)
        self.sgame.setGeometry(QtCore.QRect(200, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(15)
        self.sgame.setFont(font)
        self.sgame.setStyleSheet("background-color: transparent;")
        self.sgame.setAlignment(QtCore.Qt.AlignCenter)
        self.sgame.setObjectName("sgame")
        self.currentcps = QtWidgets.QLabel(self.page_3)
        self.currentcps.setGeometry(QtCore.QRect(10, 60, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(10)
        self.currentcps.setFont(font)
        self.currentcps.setStyleSheet("BACKGROUND-COLOR: TRANSPARENT")
        self.currentcps.setObjectName("currentcps")
        self.cps = QtWidgets.QLabel(self.page_3)
        self.cps.setGeometry(QtCore.QRect(10, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(15)
        self.cps.setFont(font)
        self.cps.setStyleSheet("BACKGROUND-COLOR: TRANSPARENT;")
        self.cps.setAlignment(QtCore.Qt.AlignCenter)
        self.cps.setObjectName("cps")
        self.pushButton = QtWidgets.QPushButton(self.page_3, clicked=lambda: self.add_click())
        self.pushButton.setGeometry(QtCore.QRect(4, 92, 291, 431))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 3px solid #B0B0B0")
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoRepeatDelay(0)
        self.pushButton.setAutoRepeatInterval(0)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page_3)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.cpsins = QtWidgets.QLabel(self.page_7)
        self.cpsins.setGeometry(QtCore.QRect(0, 110, 301, 121))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic")
        font.setPointSize(24)
        self.cpsins.setFont(font)
        self.cpsins.setStyleSheet("background-color: transparent")
        self.cpsins.setAlignment(QtCore.Qt.AlignCenter)
        self.cpsins.setObjectName("cpsins")
        self.stackedWidget.addWidget(self.page_7)
        list_window.setCentralWidget(self.centralwidget)
        self.retranslateUi(list_window)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(list_window)
        self.second = 0
        self.clicks_made = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer_)
        self._123_timer = QTimer()
        self._123_timer.timeout.connect(self.timer_123)
        self.page_ = 3

    def Start(self):
        self.stackedWidget.setCurrentIndex(1)

    def S1_list(self):
        self.second = 1
        self.cpsins.setText(f'0 CPS\n0 clicks in {self.second}S')
        self.sgame.setText(f'{self.second}S')
        self.stackedWidget.setCurrentIndex(2)
        self._123_timer.start(1000)
        self.timer.start(4000)

    def S3_list(self):
        self.second = 3
        self.cpsins.setText(f'0 CPS\n0 clicks in {self.second}S')
        self.sgame.setText(f'{self.second}S')
        self.stackedWidget.setCurrentIndex(2)
        self._123_timer.start(1000)
        self.timer.start(6000)

    def S5_list(self):
        self.second = 5
        self.cpsins.setText(f'0 CPS\n0 clicks in {self.second}S')
        self.sgame.setText(f'{self.second}S')
        self.stackedWidget.setCurrentIndex(2)
        self._123_timer.start(1000)
        self.timer.start(8000)

    def S10_list(self):
        self.second = 10
        self.cpsins.setText(f'0 CPS\n0 clicks in {self.second}S')
        self.sgame.setText(f'{self.second}S')
        self.stackedWidget.setCurrentIndex(2)
        self._123_timer.start(1000)
        self.timer.start(13000)

    def S30_list(self):
        self.second = 30
        self.cpsins.setText(f'0 CPS\n0 clicks in {self.second}S')
        self.sgame.setText(f'{self.second}S')
        self.stackedWidget.setCurrentIndex(2)
        self._123_timer.start(1000)
        self.timer.start(33000)

    def S60_list(self):
        self.second = 60
        self.cpsins.setText(f'0 CPS\n0 clicks in {self.second}S')
        self.sgame.setText(f'{self.second}S')
        self.stackedWidget.setCurrentIndex(2)
        self._123_timer.start(1000)
        self.timer.start(63000)

    def timer_(self):
        self.stackedWidget.setCurrentIndex(6)

    def timer_123(self):
        if self.page_ == 3:
            self.stackedWidget.setCurrentIndex(3)
            self.page_ -= 1
        elif self.page_ == 2:
            self.stackedWidget.setCurrentIndex(4)
            self.page_ -= 1
        elif self.page_ == 1:
            self.stackedWidget.setCurrentIndex(5)
            self.page_ -= 1

    def add_CLCiKS_MADE(self):
        c = 1
        s = self.clicks_made
        s = int(s)
        x = s + c
        self.clicks_made = int(x)
        self.cpsins.setText(
            f'{self.getCPS(self.clicks_made, self.second)} CPS\n{self.clicks_made} clicks in {self.second}S')

    def add_click(self):
        self.add_CLCiKS_MADE()
        x = int(self.pushButton.text()) + 1
        self.pushButton.setText(str(x))
        cpse = self.getCPS(int(x), self.second)
        self.cps.setText(str(cpse))

    def getCPS(self, clickss, second):
        cps_ = clickss / second
        cps_ = round(cps_, 1)
        cps_ = str(cps_)
        cps_S = cps_.split(".")
        cps_1 = int(cps_S[1])
        if cps_1 == 0:
            return str(cps_S[0])
        else:
            return cps_

    def cpsprinter(self):
        c = self.clicks_made
        s = self.second
        cps = self.getCPS(c, s)
        self.cpsins.setText(f"{cps} CPS\n{c} clicks in {s}S")

    def retranslateUi(self, list_window):
        _translate = QtCore.QCoreApplication.translate
        list_window.setWindowTitle(_translate("list_window", "CPS-Counter"))
        self.click_to_start_button.setText(_translate("list_window", "CLICK TO START"))
        self.cps_label.setText(_translate("list_window", "CPS-Counter"))
        self.s3.setText(_translate("list_window", "3S"))
        self.s1.setText(_translate("list_window", "1S"))
        self.s10.setText(_translate("list_window", "10S"))
        self.s60.setText(_translate("list_window", "60S"))
        self.s5.setText(_translate("list_window", "5S"))
        self.selecmode.setText(_translate("list_window", "SELECT MODE"))
        self.s30.setText(_translate("list_window", "30S"))
        self.in3.setText(_translate("list_window", "In 3..."))
        self.in2.setText(_translate("list_window", "In 2..."))
        self.in1.setText(_translate("list_window", "In 1..."))
        self.sgame.setText(_translate("list_window", "60S"))
        self.currentcps.setText(_translate("list_window", "CURRENT CPS"))
        self.cps.setText(_translate("list_window", "0"))
        self.pushButton.setText(_translate("list_window", "0"))
        self.cpsins.setText(_translate("list_window", "10 CPS\n"
                                                      "10 clicks in 60S"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    list_window = QtWidgets.QMainWindow()
    ui = Ui_list_window()
    ui.setupUi(list_window)
    list_window.show()
    sys.exit(app.exec_())
