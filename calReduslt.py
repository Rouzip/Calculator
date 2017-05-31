# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datastruct import *


class Ui_Form(object):

    def setupUi(self, Form):
        self.result = []
        Form.setObjectName("Form")
        Form.resize(870, 690)
        self.calEdit = QtWidgets.QLineEdit(Form)
        self.calEdit.setGeometry(QtCore.QRect(90, 30, 701, 91))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.calEdit.setFont(font)
        self.calEdit.setObjectName("calEdit")
        self.resultEdit = QtWidgets.QLineEdit(Form)
        self.resultEdit.setGeometry(QtCore.QRect(280, 150, 511, 91))
        self.resultEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resultEdit.setReadOnly(True)
        self.resultEdit.setObjectName("resultEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 290, 711, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sin_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.sin_btn.setObjectName("sin_btn")
        self.gridLayout.addWidget(self.sin_btn, 0, 0, 1, 1)
        self.cos_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.cos_btn.setObjectName("cos_btn")
        self.gridLayout.addWidget(self.cos_btn, 0, 1, 1, 1)
        self.tan_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.tan_btn.setObjectName("tan_btn")
        self.gridLayout.addWidget(self.tan_btn, 0, 2, 1, 1)
        self.mod_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.mod_btn.setObjectName("mod_btn")
        self.gridLayout.addWidget(self.mod_btn, 0, 3, 1, 1)
        self.left_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.left_btn.setObjectName("left_btn")
        self.gridLayout.addWidget(self.left_btn, 0, 4, 1, 1)
        self.right_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.right_btn.setObjectName("right_btn")
        self.gridLayout.addWidget(self.right_btn, 0, 5, 1, 1)
        self.sev_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.sev_btn.setObjectName("sev_btn")
        self.gridLayout.addWidget(self.sev_btn, 1, 0, 1, 1)
        self.eig_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.eig_btn.setObjectName("eig_btn")
        self.gridLayout.addWidget(self.eig_btn, 1, 1, 1, 1)
        self.nin_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.nin_btn.setObjectName("nin_btn")
        self.gridLayout.addWidget(self.nin_btn, 1, 2, 1, 1)
        self.div_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.div_btn.setObjectName("div_btn")
        self.gridLayout.addWidget(self.div_btn, 1, 3, 1, 1)
        self.fac_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.fac_btn.setObjectName("fac_btn")
        self.gridLayout.addWidget(self.fac_btn, 1, 4, 1, 1)
        self.pow_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.pow_btn.setObjectName("pow_btn")
        self.gridLayout.addWidget(self.pow_btn, 1, 5, 1, 1)
        self.fou_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.fou_btn.setObjectName("fou_btn")
        self.gridLayout.addWidget(self.fou_btn, 2, 0, 1, 1)
        self.fiv_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.fiv_btn.setObjectName("fiv_btn")
        self.gridLayout.addWidget(self.fiv_btn, 2, 1, 1, 1)
        self.six_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.six_btn.setObjectName("six_btn")
        self.gridLayout.addWidget(self.six_btn, 2, 2, 1, 1)
        self.mud_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.mud_btn.setObjectName("mud_btn")
        self.gridLayout.addWidget(self.mud_btn, 2, 3, 1, 1)
        self.less_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.less_btn.setObjectName("less_btn")
        self.gridLayout.addWidget(self.less_btn, 2, 4, 1, 1)
        self.more_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.more_btn.setObjectName("more_btn")
        self.gridLayout.addWidget(self.more_btn, 2, 5, 1, 1)
        self.one_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.one_btn.setObjectName("one_btn")
        self.gridLayout.addWidget(self.one_btn, 3, 0, 1, 1)
        self.two_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.two_btn.setObjectName("two_btn")
        self.gridLayout.addWidget(self.two_btn, 3, 1, 1, 1)
        self.thr_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.thr_btn.setObjectName("thr_btn")
        self.gridLayout.addWidget(self.thr_btn, 3, 2, 1, 1)
        self.plu_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.plu_btn.setObjectName("plu_btn")
        self.gridLayout.addWidget(self.plu_btn, 3, 3, 1, 1)
        self.log_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.log_btn.setObjectName("log_btn")
        self.gridLayout.addWidget(self.log_btn, 3, 4, 1, 1)
        self.sqrt_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.sqrt_btn.setObjectName("sqrt_btn")
        self.gridLayout.addWidget(self.sqrt_btn, 3, 5, 1, 1)
        self.last_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.last_btn.setObjectName("last_btn")
        self.gridLayout.addWidget(self.last_btn, 4, 0, 1, 1)
        self.zer_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.zer_btn.setObjectName("zer_btn")
        self.gridLayout.addWidget(self.zer_btn, 4, 1, 1, 1)
        self.point_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.point_btn.setObjectName("point_btn")
        self.gridLayout.addWidget(self.point_btn, 4, 2, 1, 1)
        self.dec_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.dec_btn.setObjectName("dec_btn")
        self.gridLayout.addWidget(self.dec_btn, 4, 3, 1, 1)
        self.clear_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.clear_btn.setObjectName("clear_btn")
        self.gridLayout.addWidget(self.clear_btn, 4, 4, 1, 1)
        self.result_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.result_btn.setObjectName("result_btn")
        self.gridLayout.addWidget(self.result_btn, 4, 5, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #######################事件函数##############################
        self.sin_btn.clicked.connect(appendSin)
        self.cos_btn.clicked.connect(appendCos)
        self.tan_btn.clicked.connect(appendTan)
        self.one_btn.clicked.connect(appendOne)
        self.two_btn.clicked.connect(appendTwo)
        self.thr_btn.clicked.connect(appendThr)
        self.fou_btn.clicked.connect(appendFou)
        self.fiv_btn.clicked.connect(appendFiv)
        self.six_btn.clicked.connect(appendSix)
        self.sev_btn.clicked.connect(appendSev)
        self.eig_btn.clicked.connect(appendEig)
        self.nin_btn.clicked.connect(appendNin)
        self.zer_btn.clicked.connect(appendZer)
        self.div_btn.clicked.connect(appendDiv)
        self.mud_btn.clicked.connect(appendMud)
        self.plu_btn.clicked.connect(appendPlu)
        self.dec_btn.clicked.connect(appendDec)
        self.left_btn.clicked.connect(appendLeft)
        self.right_btn.clicked.connect(appendRight)
        self.log_btn.clicked.connect(appendLog)
        self.more_btn.clicked.connect(appendMore)
        self.less_btn.clicked.connect(appendLess)
        self.sqrt_btn.clicked.connect(appendSqrt)
        self.point_btn.clicked.connect(appendPoint)
        self.pow_btn.clicked.connect(appendPow)
        self.fac_btn.clicked.connect(appendFac)

        def appendSin():
            self.calEdit.append('sin')

        def appendCos():
            self.calEdit.append('cos')

        def appendTan():
            self.calEdit.append('tan')

        def appendMod():
            self.calEdit.append('mod')

        def appendLeft():
            self.calEdit.append('(')

        def appendRight():
            self.calEdit.append(')')

        def appendOne():
            self.calEdit.append('1')

        def appendTwo():
            self.calEdit.append('2')

        def appendThr():
            self.calEdit.append('3')

        def appendFou():
            self.calEdit.append('4')

        def appendFiv():
            self.calEdit.append('5')

        def appendSix():
            self.calEdit.append('6')

        def appendSev():
            self.calEdit.append('7')

        def appendEig():
            self.calEdit.append('8')

        def appendNin():
            self.calEdit.append('9')

        def appendZer():
            self.calEdit.append('0')

        def appendPow():
            self.calEdit.append('^')

        def appendSqrt():
            self.calEdit.append('sqrt')

        def appendLog():
            self.calEdit.append('log')

        def appendFac():
            self.calEdit.append('!')

        def appendPlu():
            self.calEdit.append('+')

        def appendDec():
            self.calEdit.append('-')

        def appendMud():
            self.calEdit.append('*')

        def appendDiv():
            self.calEdit.append('/')

        def appendMore():
            self.calEdit.append('>')

        def appendLess():
            self.calEdit.append('<')

        def appendPoint():
            self.calEdit.append('.')

        def clear():
            self.calEdit.clear()

        def last():
            self.calEdit.clear()
            if result:
                self.calEdit.append(self.result.pop())
            else:
                raise print('无上次记录！')

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "="))
        self.sin_btn.setText(_translate("Form", "sin"))
        self.cos_btn.setText(_translate("Form", "cos"))
        self.tan_btn.setText(_translate("Form", "tan"))
        self.mod_btn.setText(_translate("Form", "%"))
        self.left_btn.setText(_translate("Form", "("))
        self.right_btn.setText(_translate("Form", ")"))
        self.sev_btn.setText(_translate("Form", "7"))
        self.eig_btn.setText(_translate("Form", "8"))
        self.nin_btn.setText(_translate("Form", "9"))
        self.div_btn.setText(_translate("Form", "/"))
        self.fac_btn.setText(_translate("Form", "!"))
        self.pow_btn.setText(_translate("Form", "^"))
        self.fou_btn.setText(_translate("Form", "4"))
        self.fiv_btn.setText(_translate("Form", "5"))
        self.six_btn.setText(_translate("Form", "6"))
        self.mud_btn.setText(_translate("Form", "*"))
        self.less_btn.setText(_translate("Form", "<"))
        self.more_btn.setText(_translate("Form", ">"))
        self.one_btn.setText(_translate("Form", "1"))
        self.two_btn.setText(_translate("Form", "2"))
        self.thr_btn.setText(_translate("Form", "3"))
        self.plu_btn.setText(_translate("Form", "+"))
        self.log_btn.setText(_translate("Form", "log"))
        self.sqrt_btn.setText(_translate("Form", "√"))
        self.last_btn.setText(_translate("Form", "last"))
        self.zer_btn.setText(_translate("Form", "0"))
        self.point_btn.setText(_translate("Form", "."))
        self.dec_btn.setText(_translate("Form", "-"))
        self.clear_btn.setText(_translate("Form", "clear"))
        self.result_btn.setText(_translate("Form", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
