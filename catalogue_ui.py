# Form implementation generated from reading ui file 'catalogue.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1145, 780)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_background = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_background.setGeometry(QtCore.QRect(280, 710, 1141, 720))
        self.label_background.setMaximumSize(QtCore.QSize(1280, 720))
        self.label_background.setText("")
        self.label_background.setPixmap(QtGui.QPixmap("backgroundDBMS.png"))
        self.label_background.setScaledContents(True)
        self.label_background.setObjectName("label_background")
        self.label_logo_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_logo_7.setGeometry(QtCore.QRect(0, 0, 191, 191))
        self.label_logo_7.setText("")
        self.label_logo_7.setPixmap(QtGui.QPixmap("Safatique logo (2).png"))
        self.label_logo_7.setScaledContents(True)
        self.label_logo_7.setObjectName("label_logo_7")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(40, 500, 231, 251))
        self.groupBox_7.setObjectName("groupBox_7")
        self.radioButton = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 95, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 90, 95, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 120, 95, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 150, 95, 20))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 180, 95, 20))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 210, 95, 20))
        self.radioButton_7.setObjectName("radioButton_7")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 170, 321, 311))
        font = QtGui.QFont()
        font.setFamily("Bell MT")
        font.setPointSize(14)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setObjectName("textBrowser")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(400, 50, 691, 311))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 668, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_logo_5 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_logo_5.setMaximumSize(QtCore.QSize(161, 171))
        self.label_logo_5.setText("")
        self.label_logo_5.setPixmap(QtGui.QPixmap("cruella.png"))
        self.label_logo_5.setScaledContents(True)
        self.label_logo_5.setObjectName("label_logo_5")
        self.gridLayout_5.addWidget(self.label_logo_5, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_logo_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_logo_3.setMaximumSize(QtCore.QSize(161, 171))
        self.label_logo_3.setText("")
        self.label_logo_3.setPixmap(QtGui.QPixmap("charms1.jpg"))
        self.label_logo_3.setScaledContents(True)
        self.label_logo_3.setObjectName("label_logo_3")
        self.gridLayout_3.addWidget(self.label_logo_3, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_logo_6 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_logo_6.setMaximumSize(QtCore.QSize(161, 171))
        self.label_logo_6.setText("")
        self.label_logo_6.setPixmap(QtGui.QPixmap("greenheart.png"))
        self.label_logo_6.setScaledContents(True)
        self.label_logo_6.setObjectName("label_logo_6")
        self.gridLayout_6.addWidget(self.label_logo_6, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_12.setObjectName("label_12")
        self.gridLayout_6.addWidget(self.label_12, 2, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_logo = QtWidgets.QLabel(parent=self.groupBox)
        self.label_logo.setMaximumSize(QtCore.QSize(161, 171))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap("earrings.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.gridLayout.addWidget(self.label_logo, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_logo_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_logo_2.setMaximumSize(QtCore.QSize(161, 171))
        self.label_logo_2.setText("")
        self.label_logo_2.setPixmap(QtGui.QPixmap("bracelets.jpg"))
        self.label_logo_2.setScaledContents(True)
        self.label_logo_2.setObjectName("label_logo_2")
        self.gridLayout_2.addWidget(self.label_logo_2, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_logo_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_logo_4.setMaximumSize(QtCore.QSize(161, 171))
        self.label_logo_4.setText("")
        self.label_logo_4.setPixmap(QtGui.QPixmap("heartnecklace1.jpg"))
        self.label_logo_4.setScaledContents(True)
        self.label_logo_4.setObjectName("label_logo_4")
        self.gridLayout_4.addWidget(self.label_logo_4, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        # Create a vertical layout for the scrollable content
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)

        # Add each group box to the layout
        self.scrollAreaLayout.addWidget(self.groupBox)
        self.scrollAreaLayout.addWidget(self.groupBox_2)
        self.scrollAreaLayout.addWidget(self.groupBox_3)
        self.scrollAreaLayout.addWidget(self.groupBox_4)
        self.scrollAreaLayout.addWidget(self.groupBox_5)
        self.scrollAreaLayout.addWidget(self.groupBox_6)

        # Apply the layout to scrollAreaWidgetContents
        self.scrollAreaWidgetContents.setLayout(self.scrollAreaLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Categories"))
        self.radioButton.setText(_translate("MainWindow", "Bracelts"))
        self.radioButton_2.setText(_translate("MainWindow", "Necklaces"))
        self.radioButton_3.setText(_translate("MainWindow", "Earrings"))
        self.radioButton_4.setText(_translate("MainWindow", "Charms"))
        self.radioButton_5.setText(_translate("MainWindow", "Pendants"))
        self.radioButton_6.setText(_translate("MainWindow", "Keychains"))
        self.radioButton_7.setText(_translate("MainWindow", "Bundles"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Bell MT\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Welcome to Safatique, your destination for handmade jewelry that transforms everyday moments into fairytale dreams. Embrace the Princess Core aesthetic with our uniquely crafted pieces designed to make you feel like royalty. Each item is meticulously created to add a touch of drama and elegance to your style. Discover the magic of being extraordinary with Safatique.</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "Cruella Bracelet"))
        self.label_11.setText(_translate("MainWindow", "Rs. 300"))
        self.label_3.setText(_translate("MainWindow", "Kuromi Charm"))
        self.label_9.setText(_translate("MainWindow", "Rs. 550"))
        self.label_6.setText(_translate("MainWindow", "Heart Pendant"))
        self.label_12.setText(_translate("MainWindow", "Rs. 600"))
        self.label.setText(_translate("MainWindow", "Earrings"))
        self.label_7.setText(_translate("MainWindow", "Rs. 370"))
        self.label_2.setText(_translate("MainWindow", "Bracelet"))
        self.label_8.setText(_translate("MainWindow", "Rs. 300"))
        self.label_4.setText(_translate("MainWindow", "Heart Necklace"))
        self.label_10.setText(_translate("MainWindow", "Rs. 600"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())