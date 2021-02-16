# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res\about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_aboutAutoSplitWidget(object):
    def setupUi(self, aboutAutoSplitWidget):
        aboutAutoSplitWidget.setObjectName("aboutAutoSplitWidget")
        aboutAutoSplitWidget.resize(276, 249)
        aboutAutoSplitWidget.setMinimumSize(QtCore.QSize(276, 249))
        aboutAutoSplitWidget.setMaximumSize(QtCore.QSize(276, 249))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        aboutAutoSplitWidget.setWindowIcon(icon)
        self.okButton = QtWidgets.QPushButton(aboutAutoSplitWidget)
        self.okButton.setGeometry(QtCore.QRect(190, 220, 71, 21))
        self.okButton.setObjectName("okButton")
        self.createdbyLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.createdbyLabel.setGeometry(QtCore.QRect(10, 44, 151, 16))
        self.createdbyLabel.setObjectName("createdbyLabel")
        self.versionLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.versionLabel.setGeometry(QtCore.QRect(10, 21, 71, 16))
        self.versionLabel.setObjectName("versionLabel")
        self.donatetextLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.donatetextLabel.setGeometry(QtCore.QRect(46, 95, 191, 41))
        self.donatetextLabel.setObjectName("donatetextLabel")
        self.donatebuttonLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.donatebuttonLabel.setGeometry(QtCore.QRect(52, 127, 171, 91))
        self.donatebuttonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.donatebuttonLabel.setObjectName("donatebuttonLabel")
        self.iconLabel = QtWidgets.QLabel(aboutAutoSplitWidget)
        self.iconLabel.setGeometry(QtCore.QRect(190, 17, 62, 71))
        self.iconLabel.setObjectName("iconLabel")

        self.retranslateUi(aboutAutoSplitWidget)
        self.okButton.clicked.connect(aboutAutoSplitWidget.close)
        QtCore.QMetaObject.connectSlotsByName(aboutAutoSplitWidget)

    def retranslateUi(self, aboutAutoSplitWidget):
        _translate = QtCore.QCoreApplication.translate
        aboutAutoSplitWidget.setWindowTitle(_translate("aboutAutoSplitWidget", "About AutoSplit"))
        self.okButton.setText(_translate("aboutAutoSplitWidget", "OK"))
        self.createdbyLabel.setText(_translate("aboutAutoSplitWidget", "<html><head/><body><p>Created by <a href=\"https://twitter.com/toufool\"><span style=\" text-decoration: underline; color:#0000ff;\">Toufool</span></a> and <a href=\"https://twitter.com/faschz\"><span style=\" text-decoration: underline; color:#0000ff;\">Faschz</span></a></p></body></html>"))
        self.versionLabel.setText(_translate("aboutAutoSplitWidget", "Version: 1.2.0"))
        self.donatetextLabel.setText(_translate("aboutAutoSplitWidget", "If you enjoy using this program, please\n"
"       consider donating. Thank you!"))
        self.donatebuttonLabel.setText(_translate("aboutAutoSplitWidget", "<html><head/><body><p><a href=\"https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=BYRHQG69YRHBA&item_name=AutoSplit+development&currency_code=USD&source=url\"><img src=\":/resources/donatebutton.png\"/></p></body></html>"))
        self.iconLabel.setText(_translate("aboutAutoSplitWidget", "<html><head/><body><p><img src=\":/resources/icon.ico\"/></p></body></html>"))

# import resources_rc
