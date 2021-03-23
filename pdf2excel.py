# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pdf2excel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 459)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.captchaValue = QtWidgets.QLineEdit(self.centralwidget)
        self.captchaValue.setObjectName("captchaValue")
        self.gridLayout.addWidget(self.captchaValue, 10, 1, 1, 1)
        self.chromeUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.chromeUrl.setObjectName("chromeUrl")
        self.gridLayout.addWidget(self.chromeUrl, 5, 1, 1, 1)
        self.checkBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBtn.sizePolicy().hasHeightForWidth())
        self.checkBtn.setSizePolicy(sizePolicy)
        self.checkBtn.setObjectName("checkBtn")
        self.gridLayout.addWidget(self.checkBtn, 10, 3, 1, 1)
        self.chromeLabel = QtWidgets.QLabel(self.centralwidget)
        self.chromeLabel.setObjectName("chromeLabel")
        self.gridLayout.addWidget(self.chromeLabel, 5, 0, 1, 1)
        self.captchaLabel = QtWidgets.QLabel(self.centralwidget)
        self.captchaLabel.setObjectName("captchaLabel")
        self.gridLayout.addWidget(self.captchaLabel, 10, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.captchaImgLabel = QtWidgets.QLabel(self.centralwidget)
        self.captchaImgLabel.setMaximumSize(QtCore.QSize(180, 75))
        self.captchaImgLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.captchaImgLabel.setText("")
        self.captchaImgLabel.setObjectName("captchaImgLabel")
        self.horizontalLayout_2.addWidget(self.captchaImgLabel)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 1, 1, 1)
        self.runChromeBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.runChromeBtn.sizePolicy().hasHeightForWidth())
        self.runChromeBtn.setSizePolicy(sizePolicy)
        self.runChromeBtn.setObjectName("runChromeBtn")
        self.gridLayout.addWidget(self.runChromeBtn, 5, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushBtn.sizePolicy().hasHeightForWidth())
        self.pushBtn.setSizePolicy(sizePolicy)
        self.pushBtn.setObjectName("pushBtn")
        self.horizontalLayout.addWidget(self.pushBtn)
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextBtn.sizePolicy().hasHeightForWidth())
        self.nextBtn.setSizePolicy(sizePolicy)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout.addWidget(self.nextBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 14, 1, 1, 1)
        self.gridLayout2 = QtWidgets.QGridLayout()
        self.gridLayout2.setObjectName("gridLayout2")
        self.startCheckBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startCheckBtn.sizePolicy().hasHeightForWidth())
        self.startCheckBtn.setSizePolicy(sizePolicy)
        self.startCheckBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startCheckBtn.setObjectName("startCheckBtn")
        self.gridLayout2.addWidget(self.startCheckBtn, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout2, 6, 1, 1, 1)
        self.gridLayout1 = QtWidgets.QGridLayout()
        self.gridLayout1.setObjectName("gridLayout1")
        self.parsePdfBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parsePdfBtn.sizePolicy().hasHeightForWidth())
        self.parsePdfBtn.setSizePolicy(sizePolicy)
        self.parsePdfBtn.setObjectName("parsePdfBtn")
        self.gridLayout1.addWidget(self.parsePdfBtn, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout1, 2, 1, 1, 1)
        self.captchaTextLabel = QtWidgets.QLabel(self.centralwidget)
        self.captchaTextLabel.setText("")
        self.captchaTextLabel.setWordWrap(True)
        self.captchaTextLabel.setObjectName("captchaTextLabel")
        self.gridLayout.addWidget(self.captchaTextLabel, 8, 3, 1, 1)
        self.currentCheckLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentCheckLabel.setText("")
        self.currentCheckLabel.setObjectName("currentCheckLabel")
        self.gridLayout.addWidget(self.currentCheckLabel, 11, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.runChromeBtn.clicked.connect(MainWindow.run_chrome)
        self.parsePdfBtn.clicked.connect(MainWindow.pdf2text)
        self.checkBtn.clicked.connect(MainWindow.check_captcha)
        self.nextBtn.clicked.connect(MainWindow.next)
        self.startCheckBtn.clicked.connect(MainWindow.start_check)
        self.pushBtn.clicked.connect(MainWindow.previous)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.chromeUrl.setText(_translate("MainWindow", "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"))
        self.checkBtn.setText(_translate("MainWindow", "查验"))
        self.chromeLabel.setText(_translate("MainWindow", "Chrome地址"))
        self.captchaLabel.setText(_translate("MainWindow", "验证码"))
        self.runChromeBtn.setText(_translate("MainWindow", "运行chrome"))
        self.pushBtn.setText(_translate("MainWindow", "上一个"))
        self.nextBtn.setText(_translate("MainWindow", "下一个"))
        self.startCheckBtn.setText(_translate("MainWindow", "开始查验"))
        self.parsePdfBtn.setText(_translate("MainWindow", "解析发票"))
