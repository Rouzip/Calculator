# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cal.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datastruct import *
from collections import deque


class Ui_calculate(object):

    def setupUi(self, calculate):

        def appendSin():
            self.calEdit.clear()
            self.calContent += 'sin('
            self.calEdit.append(self.calContent)

        def appendCos():
            self.calEdit.clear()
            self.calContent += 'cos('
            self.calEdit.append(self.calContent)

        def appendTan():
            self.calEdit.clear()
            self.calContent += 'tan('
            self.calEdit.append(self.calContent)

        def appendMod():
            self.calEdit.clear()
            self.calContent += '%'
            self.calEdit.append(self.calContent)

        def appendLeft():
            self.calEdit.clear()
            self.calContent += '('
            self.calEdit.append(self.calContent)

        def appendRight():
            self.calEdit.clear()
            self.calContent += ')'
            self.calEdit.append(self.calContent)

        def appendOne():
            self.calEdit.clear()
            self.calContent += '1'
            self.calEdit.append(self.calContent)

        def appendTwo():
            self.calEdit.clear()
            self.calContent += '2'
            self.calEdit.append(self.calContent)

        def appendThr():
            self.calEdit.clear()
            self.calContent += '3'
            self.calEdit.append(self.calContent)

        def appendFou():
            self.calEdit.clear()
            self.calContent += '4'
            self.calEdit.append(self.calContent)

        def appendFiv():
            self.calEdit.clear()
            self.calContent += '5'
            self.calEdit.append(self.calContent)

        def appendSix():
            self.calEdit.clear()
            self.calContent += '6'
            self.calEdit.append(self.calContent)

        def appendSev():
            self.calEdit.clear()
            self.calContent += '7'
            self.calEdit.append(self.calContent)

        def appendEig():
            self.calEdit.clear()
            self.calContent += '8'
            self.calEdit.append(self.calContent)

        def appendNin():
            self.calEdit.clear()
            self.calContent += '9'
            self.calEdit.append(self.calContent)

        def appendZer():
            self.calEdit.clear()
            self.calContent += '0'
            self.calEdit.append(self.calContent)

        def appendPow():
            self.calEdit.clear()
            self.calContent += '^'
            self.calEdit.append(self.calContent)

        def appendSqrt():
            self.calEdit.clear()
            self.calContent += 'sqrt('
            self.calEdit.append(self.calContent)

        def appendLog():
            self.calEdit.clear()
            self.calContent += 'log('
            self.calEdit.append(self.calContent)

        def appendFac():
            self.calEdit.clear()
            self.calContent += '!'
            self.calEdit.append(self.calContent)

        def appendPlu():
            self.calEdit.clear()
            self.calContent += '+'
            self.calEdit.append(self.calContent)

        def appendDec():
            self.calEdit.clear()
            self.calContent += '-'
            self.calEdit.append(self.calContent)

        def appendMud():
            self.calEdit.clear()
            self.calContent += '*'
            self.calEdit.append(self.calContent)

        def appendDiv():
            self.calEdit.clear()
            self.calContent += '/'
            self.calEdit.append(self.calContent)

        def appendMore():
            self.calEdit.clear()
            self.calContent += '>'
            self.calEdit.append(self.calContent)

        def appendLess():
            self.calEdit.clear()
            self.calContent += '<'
            self.calEdit.append(self.calContent)

        def appendPoint():
            self.calEdit.clear()
            self.calContent += '.'
            self.calEdit.append(self.calContent)

        def clear():
            self.calContent = ''
            self.calEdit.clear()

        # 计算出结果，将结果添加到结果展示栏，并将结果入栈
        def result():
            try:
                if not self.calContent:
                    return
                self.resultEdit.clear()
                showResult = str(getPostfix(self.calContent))
                self.resultEdit.append(showResult)
                self.calContent = ''
                self.results.append(showResult)
            except Exception as e:
                logging.exception(e)
                self.resultEdit.clear()
                self.resultEdit.append('Error')

        def last():
            if self.results:
                self.resultEdit.clear()
                self.resultEdit.append(self.results.pop())
            else:
                self.resultEdit.clear()
                self.resultEdit.append('您还未进行运算！')

        self.calContent = ''
        self.results = deque()
        calculate.setObjectName("calculate")
        calculate.resize(870, 690)
        self.label = QtWidgets.QLabel(calculate)
        self.label.setGeometry(QtCore.QRect(110, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(31)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(calculate)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 290, 737, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(45)
        self.gridLayout.setVerticalSpacing(36)
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
        self.calEdit = QtWidgets.QTextEdit(calculate)
        self.calEdit.setGeometry(QtCore.QRect(80, 50, 691, 78))
        self.calEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.calEdit.setReadOnly(True)
        self.calEdit.setObjectName("calEdit")
        self.resultEdit = QtWidgets.QTextEdit(calculate)
        self.resultEdit.setGeometry(QtCore.QRect(173, 170, 591, 78))
        self.resultEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resultEdit.setReadOnly(True)
        self.resultEdit.setObjectName("resultEdit")

        self.retranslateUi(calculate)
        QtCore.QMetaObject.connectSlotsByName(calculate)

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
        self.mod_btn.clicked.connect(appendMod)
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
        self.clear_btn.clicked.connect(clear)
        self.result_btn.clicked.connect(result)
        self.last_btn.clicked.connect(last)

    def retranslateUi(self, calculate):
        _translate = QtCore.QCoreApplication.translate
        calculate.setWindowTitle(_translate("calculate", "计算器"))
        self.label.setText(_translate("calculate", "="))
        self.sin_btn.setText(_translate("calculate", "sin"))
        self.cos_btn.setText(_translate("calculate", "cos"))
        self.tan_btn.setText(_translate("calculate", "tan"))
        self.mod_btn.setText(_translate("calculate", "%"))
        self.left_btn.setText(_translate("calculate", "("))
        self.right_btn.setText(_translate("calculate", ")"))
        self.sev_btn.setText(_translate("calculate", "7"))
        self.eig_btn.setText(_translate("calculate", "8"))
        self.nin_btn.setText(_translate("calculate", "9"))
        self.div_btn.setText(_translate("calculate", "/"))
        self.fac_btn.setText(_translate("calculate", "!"))
        self.pow_btn.setText(_translate("calculate", "^"))
        self.fou_btn.setText(_translate("calculate", "4"))
        self.fiv_btn.setText(_translate("calculate", "5"))
        self.six_btn.setText(_translate("calculate", "6"))
        self.mud_btn.setText(_translate("calculate", "*"))
        self.less_btn.setText(_translate("calculate", "<"))
        self.more_btn.setText(_translate("calculate", ">"))
        self.one_btn.setText(_translate("calculate", "1"))
        self.two_btn.setText(_translate("calculate", "2"))
        self.thr_btn.setText(_translate("calculate", "3"))
        self.plu_btn.setText(_translate("calculate", "+"))
        self.log_btn.setText(_translate("calculate", "log"))
        self.sqrt_btn.setText(_translate("calculate", "√"))
        self.last_btn.setText(_translate("calculate", "last"))
        self.zer_btn.setText(_translate("calculate", "0"))
        self.point_btn.setText(_translate("calculate", "."))
        self.dec_btn.setText(_translate("calculate", "-"))
        self.clear_btn.setText(_translate("calculate", "clear"))
        self.result_btn.setText(_translate("calculate", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    calculate = QtWidgets.QWidget()
    ui = Ui_calculate()
    ui.setupUi(calculate)
    calculate.show()
    sys.exit(app.exec_())
