# Form implementation generated from reading ui file '4add_qlhd.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(694, 0)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 690, 708))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 60))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../IMG/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 57))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet("color: rgb(85, 170, 255);\n"
"font: 18pt \"Swis721 Blk BT\";")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.formLayout_2.setContentsMargins(20, 10, 20, 0)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(45, 45))
        self.pushButton_2.setMaximumSize(QtCore.QSize(45, 45))
        self.pushButton_2.setStyleSheet("border-color: rgb(0, 0, 255);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../IMG/settings.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pushButton_2)
        self.label_4 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(140, 40))
        self.label_4.setMaximumSize(QtCore.QSize(300, 40))
        self.label_4.setStyleSheet("border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 127, 236), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(255, 0, 0);\n"
"font: 81 15pt \"Rockwell Extra Bold\";")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.pushButton_5.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QtCore.QSize(500, 40))
        self.pushButton_5.setStyleSheet("font: 10pt \"Swis721 Blk BT\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);\n"
"border-color: rgb(120, 120, 120);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setMaximumSize(QtCore.QSize(500, 40))
        self.pushButton_6.setStyleSheet("background-color: rgb(148, 148, 111);\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"Swis721 Blk BT\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.pushButton_6)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetMinimumSize)
        self.formLayout.setContentsMargins(10, 5, 10, 5)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy)
        self.textEdit_2.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_2)
        self.label_15 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setStyleSheet("font: 10pt \"Bauhaus 93\";")
        self.label_15.setObjectName("label_15")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_15)
        self.textEdit = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.textEdit_3 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        self.textEdit_3.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_3.setObjectName("textEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_3)
        self.label_7 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_7.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.label_6 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_6.setStyleSheet("font: 10pt \"Swis721 Blk BT\";\n"
"")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.label_8 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_8.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_9.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.textEdit_9 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_9.sizePolicy().hasHeightForWidth())
        self.textEdit_9.setSizePolicy(sizePolicy)
        self.textEdit_9.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_9.setObjectName("textEdit_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_9)
        self.label_10 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_10.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.textEdit_8 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_8.sizePolicy().hasHeightForWidth())
        self.textEdit_8.setSizePolicy(sizePolicy)
        self.textEdit_8.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_8.setObjectName("textEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_8)
        self.label_12 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_12.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_12)
        self.textEdit_7 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy)
        self.textEdit_7.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_7.setObjectName("textEdit_7")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_7)
        self.label_13 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_13.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_13.setObjectName("label_13")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_13)
        self.textEdit_6 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_6.sizePolicy().hasHeightForWidth())
        self.textEdit_6.setSizePolicy(sizePolicy)
        self.textEdit_6.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_6.setObjectName("textEdit_6")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_6)
        self.textEdit_14 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_14.sizePolicy().hasHeightForWidth())
        self.textEdit_14.setSizePolicy(sizePolicy)
        self.textEdit_14.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_14.setObjectName("textEdit_14")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_14)
        self.label_14 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_14.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_14)
        self.textEdit_13 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_13.sizePolicy().hasHeightForWidth())
        self.textEdit_13.setSizePolicy(sizePolicy)
        self.textEdit_13.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_13.setObjectName("textEdit_13")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_13)
        self.label_11 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_11.setStyleSheet("font: 10pt \"Swis721 Blk BT\";")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_11)
        self.textEdit_4 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setMaximumSize(QtCore.QSize(300, 40))
        self.textEdit_4.setObjectName("textEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.textEdit_4)
        self.calendarWidget_4 = QtWidgets.QCalendarWidget(parent=self.verticalLayoutWidget)
        self.calendarWidget_4.setMaximumSize(QtCore.QSize(300, 40))
        self.calendarWidget_4.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.calendarWidget_4.setObjectName("calendarWidget_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.calendarWidget_4)
        self.calendarWidget_3 = QtWidgets.QCalendarWidget(parent=self.verticalLayoutWidget)
        self.calendarWidget_3.setMaximumSize(QtCore.QSize(300, 40))
        self.calendarWidget_3.setStyleSheet("background-color: rgb(190, 190, 190);")
        self.calendarWidget_3.setObjectName("calendarWidget_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.calendarWidget_3)
        self.horizontalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ADD_HỢP ĐỒNG"))
        self.label.setText(_translate("Dialog", "\n"
"CONTRACT MANAGEMENT"))
        self.label_4.setText(_translate("Dialog", "FUCNTION"))
        self.pushButton_5.setText(_translate("Dialog", "CREATE LABOR CONTRACT"))
        self.pushButton_6.setText(_translate("Dialog", "VIEW LABOR CONTRACT"))
        self.label_3.setText(_translate("Dialog", "MHD:"))
        self.label_15.setText(_translate("Dialog", "MNS:"))
        self.label_5.setText(_translate("Dialog", "LOAIHD:"))
        self.label_7.setText(_translate("Dialog", "VITRI:"))
        self.label_6.setText(_translate("Dialog", "NGAYKY:"))
        self.label_8.setText(_translate("Dialog", "NGAYKT:"))
        self.label_9.setText(_translate("Dialog", "THOIHANHD:"))
        self.label_10.setText(_translate("Dialog", "LUONGCB:"))
        self.label_12.setText(_translate("Dialog", "PHUCAP:"))
        self.label_13.setText(_translate("Dialog", "BAOHIEM:"))
        self.label_14.setText(_translate("Dialog", "DKKTHD:"))
        self.label_11.setText(_translate("Dialog", "DKKL:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
