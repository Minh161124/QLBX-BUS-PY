# Form implementation generated from reading ui file '7view_qlccvlt.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(883, 0)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 881, 370))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_3.setMaximumSize(QtCore.QSize(90, 45))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../IMG/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(90, 45))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet("color: rgb(85, 170, 255);\n"
"font: 18pt \"Swis721 Blk BT\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textEdit_7 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy)
        self.textEdit_7.setMaximumSize(QtCore.QSize(250, 53))
        self.textEdit_7.setObjectName("textEdit_7")
        self.horizontalLayout_3.addWidget(self.textEdit_7)
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_8.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_8.setMaximumSize(QtCore.QSize(140, 40))
        self.pushButton_8.setStatusTip("")
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border-color: rgb(0, 85, 255);\n"
"font: 10pt \"Gill Sans Ultra Bold Condensed\";")
        self.pushButton_8.setAutoDefault(True)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_9.setMaximumSize(QtCore.QSize(120, 40))
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border-color: rgb(0, 85, 255);\n"
"font: 10pt \"Gill Sans Ultra Bold Condensed\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_4.setMaximumSize(QtCore.QSize(140, 40))
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border-color: rgb(0, 85, 255);\n"
"font: 10pt \"Gill Sans Ultra Bold Condensed\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMinimumSize(QtCore.QSize(75, 23))
        self.pushButton_7.setMaximumSize(QtCore.QSize(120, 40))
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border-color: rgb(0, 85, 255);\n"
"font: 10pt \"Gill Sans Ultra Bold Condensed\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.formLayout_4.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout_4.setContentsMargins(20, 10, 20, 20)
        self.formLayout_4.setHorizontalSpacing(15)
        self.formLayout_4.setVerticalSpacing(20)
        self.formLayout_4.setObjectName("formLayout_4")
        self.view_ns = QtWidgets.QTableWidget(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view_ns.sizePolicy().hasHeightForWidth())
        self.view_ns.setSizePolicy(sizePolicy)
        self.view_ns.setMaximumSize(QtCore.QSize(2000, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.view_ns.setFont(font)
        self.view_ns.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.view_ns.setShowGrid(True)
        self.view_ns.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.view_ns.setCornerButtonEnabled(False)
        self.view_ns.setRowCount(2)
        self.view_ns.setColumnCount(11)
        self.view_ns.setObjectName("view_ns")
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.view_ns.setHorizontalHeaderItem(10, item)
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.view_ns)
        self.horizontalLayout_6.addLayout(self.formLayout_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "VIEW_CCVLT"))
        self.label_2.setText(_translate("Dialog", "MANAGEMENT OF ATTENDANCE AND REWARDS"))
        self.textEdit_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"C:\\BTL Python\\CODE\\IMG\\search.png\" /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_8.setText(_translate("Dialog", "  VIEW CONTENT "))
        self.pushButton_9.setText(_translate("Dialog", "  EDIT CONTENT"))
        self.pushButton_4.setText(_translate("Dialog", "CREATE CONTENT"))
        self.pushButton_7.setText(_translate("Dialog", "DELETE CONTENT"))
        item = self.view_ns.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "1"))
        item = self.view_ns.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "MCC"))
        item = self.view_ns.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "MNS"))
        item = self.view_ns.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "NCC"))
        item = self.view_ns.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "CALAM"))
        item = self.view_ns.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "TTLV"))
        item = self.view_ns.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "LUONGCB"))
        item = self.view_ns.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "SONGAYCONG"))
        item = self.view_ns.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "PHUCAP"))
        item = self.view_ns.horizontalHeaderItem(8)
        item.setText(_translate("Dialog", "THUONG"))
        item = self.view_ns.horizontalHeaderItem(9)
        item.setText(_translate("Dialog", "PHAT"))
        item = self.view_ns.horizontalHeaderItem(10)
        item.setText(_translate("Dialog", "TONGLUONG"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
