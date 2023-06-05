import kalkulator_obuchni
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import math

class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = kalkulator_obuchni.Ui_MainWindow() # Экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)     # Инициализация GUI
        self.ui.new_number.setText('0')
        self.run()


    def run(self):
        self.ui.zero.clicked.connect(lambda: self.number('0'))
        self.ui.one.clicked.connect(lambda: self.number('1'))
        self.ui.two.clicked.connect(lambda: self.number('2'))
        self.ui.three.clicked.connect(lambda: self.number('3'))
        self.ui.four.clicked.connect(lambda: self.number('4'))
        self.ui.five.clicked.connect(lambda: self.number('5'))
        self.ui.sixe.clicked.connect(lambda: self.number('6'))
        self.ui.seven.clicked.connect(lambda: self.number('7'))
        self.ui.eight.clicked.connect(lambda: self.number('8'))
        self.ui.nine.clicked.connect(lambda: self.number('9'))

        self.ui.plus.clicked.connect(lambda: self.number('+'))
        self.ui.minus.clicked.connect(lambda: self.number('-'))
        self.ui.umnohit.clicked.connect(lambda: self.number('*'))
        self.ui.podelit.clicked.connect(lambda: self.number('/'))
        self.ui.stepen.clicked.connect(lambda: self.number('^'))
        self.ui.koren.clicked.connect(lambda: self.number('√'))

        self.ui.zapetai.clicked.connect(lambda: self.number(','))
        self.ui.otvet.clicked.connect(lambda: self.number('='))

        self.ui.delete_2.clicked.connect(lambda: self.number('<'))
        self.ui.delete_all.clicked.connect(lambda: self.number('C'))

        self.ui.reverse.clicked.connect(lambda: self.number('+-'))
        self.ui.faktorial.clicked.connect(lambda: self.number('!'))

        self.ui.pi.clicked.connect(lambda: self.number('pi'))
        self.ui.ee.clicked.connect(lambda: self.number('e'))

    def number(self, num):
        if self.ui.new_number.text() == 'Деление на ноль невозможно':
            self.ui.old_number.setText('')
            self.ui.new_number.setText('0')

        if num == '+' or num == '-' or num == '*' or num == '/' or num == '=' or num == '^':
            if self.ui.old_number.text() == '':
                self.ui.old_number.setText(self.ui.new_number.text() + num)
                self.ui.new_number.setText('0')
            elif '=' in self.ui.old_number.text():
                self.ui.old_number.setText(self.ui.new_number.text() + num)
                self.ui.new_number.setText('0')
            else:
                old = self.ui.old_number.text()
                new = self.ui.new_number.text()
                numer = old[-1]
                old = old[:len(old) - 1]
                old = old.replace(',', '.')
                new = new.replace(',', '.')

                if numer == '+':
                    res = float(old) + float(new)

                elif numer == '-':
                    res = float(old) - float(new)

                elif numer == '*':
                    res = float(old) * float(new)

                elif numer == '/':
                    # Деление на ноль невозможно
                    if new == '0':
                        res = 'Деление на ноль невозможно'
                    else:
                        res = float(old) / float(new)

                elif numer == '^':
                    res = float(math.pow(float(old), float(new)))

                if str(res)[-1] == '0' and str(res)[-2] == '.':
                    res = str(res)[:len(str(res)) - 2]

                old = old.replace('.', ',')
                new = new.replace('.', ',')
                res = str(res).replace('.', ',')

                if num == '=':
                    self.ui.old_number.setText(self.ui.old_number.text() + self.ui.new_number.text() + '=')
                    self.ui.new_number.setText(str(res))
                elif res == 'Деление на ноль невозможно':
                    self.ui.old_number.setText(str(old) + '/' + str(new) + '=')
                    self.ui.new_number.setText('Деление на ноль невозможно')
                else:
                    self.ui.new_number.setText('0')
                    self.ui.old_number.setText(str(res) + num)  # f'<html><head/><body><p align="right"><span style=" font-size:14pt;">{str(res) + num}</span></p></body></html>')

        elif num == '<' or num == 'C' or num == '+-' or num == '√' or num == '!' or num == 'pi' or num == 'e':
            if num =='<':
                if self.ui.new_number.text() != '0':
                    if len(self.ui.new_number.text()) == 1:
                        self.ui.new_number.setText('0')
                    else:
                        self.ui.new_number.setText(self.ui.new_number.text()[:len(self.ui.new_number.text()) - 1])

            elif num == 'C':
                self.ui.new_number.setText('0')
                self.ui.old_number.setText('')

            elif num == '+-':
                if self.ui.new_number.text()[0] == '-':
                    self.ui.new_number.setText(self.ui.new_number.text()[1:])
                else:
                    self.ui.new_number.setText('-' + self.ui.new_number.text())

            elif num == '√':
                self.ui.old_number.setText('2' + '√' + self.ui.new_number.text() + '=')

                res = float(math.sqrt(int(self.ui.new_number.text())))

                if str(res)[-1] == '0' and str(res)[-2] == '.':
                    res = str(res)[:len(str(res)) - 2]

                self.ui.new_number.setText(str(res))

            elif num == '!':
                self.ui.old_number.setText('!' + self.ui.new_number.text() + '=')
                self.ui.new_number.setText(str(math.factorial(int(self.ui.new_number.text()))))

            elif num == 'pi':
                self.ui.new_number.setText(str(math.pi))

            elif num == 'e':
                self.ui.new_number.setText(str(math.e))
        else:
            if self.ui.old_number.text() == '' and self.ui.new_number.text() == '0' or self.ui.new_number.text() == '-0' and num != ',':
                self.ui.new_number.setText(num)
            else:
                if self.ui.new_number.text() == '0' or self.ui.new_number.text() == '-0' and num != ',':
                    self.ui.new_number.setText(num)
                else:
                    numr = self.ui.new_number.text()
                    self.ui.new_number.setText(numr + num)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())