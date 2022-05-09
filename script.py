#imports
from PyQt5 import QtCore, QtGui, QtWidgets
from Taschenrechner import Ui_MainWindow
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
check = True



#logic
def zero():
    ui.lineEdit.setText(ui.lineEdit.text() + "0")
def eins():
    ui.lineEdit.setText(ui.lineEdit.text() + "1")
def zwei():
    ui.lineEdit.setText(ui.lineEdit.text() + "2")
def drei():
    ui.lineEdit.setText(ui.lineEdit.text() + "3")
def vier():
    ui.lineEdit.setText(ui.lineEdit.text() + "4")
def funf():
    ui.lineEdit.setText(ui.lineEdit.text() + "5")
def sechs():
    ui.lineEdit.setText(ui.lineEdit.text() + "6")
def sieben():
    ui.lineEdit.setText(ui.lineEdit.text() + "7")
def acht():
    ui.lineEdit.setText(ui.lineEdit.text() + "8")
def neun():
    ui.lineEdit.setText(ui.lineEdit.text() + "9")
def link_Klammer():
    ui.lineEdit.setText(ui.lineEdit.text() + "(")
def recht_Klammer():
    ui.lineEdit.setText(ui.lineEdit.text() + ")")
def Punkt():
    ui.lineEdit.setText(ui.lineEdit.text() + ".")

#operation
def plus():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "+")
    check = False

def multiple():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "*")
    check = False

def durch():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "/")
    check = False

def minus():
    global check
    ui.lineEdit.setText(ui.lineEdit.text() + "-")
    check = False


def clear():
    ui.lineEdit.setText("")
    check = True

def delete():
    ui.lineEdit.setText(ui.lineEdit.text()[0:-1])

#Ergebniss
def equals():
    global check
    global Total_rechnen
    try:
        ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
        check=False
    except ZeroDivisionError:
        ui.lineEdit.setText("Sorry ! You are dividing by zero ")
    except SyntaxError:
        ui.lineEdit.setText("Invalid ! Operation ")
    except :
        ui.lineEdit.setText("Error ")


#verbindung mit function
ui.Button_0.clicked.connect(zero)
ui.Button_1.clicked.connect(eins)
ui.Button_2.clicked.connect(zwei)
ui.Button_3.clicked.connect(drei)
ui.Button_4.clicked.connect(vier)
ui.Button_5.clicked.connect(funf)
ui.Button_6.clicked.connect(sechs)
ui.Button_7.clicked.connect(sieben)
ui.Button_8.clicked.connect(acht)
ui.Button_9.clicked.connect(neun)

ui.Button_plus.clicked.connect(plus)
ui.Button_minus.clicked.connect(minus)
ui.Button_multiple.clicked.connect(multiple)
ui.Button_durch.clicked.connect(durch)
ui.Button_link_Klammer.clicked.connect(link_Klammer)
ui.Button_recht_Klammer_2.clicked.connect(recht_Klammer)
ui.Button_Punkt.clicked.connect(Punkt)
ui.Button_clear.clicked.connect(clear)
ui.Button_delete.clicked.connect(delete)
ui.Button_equals.clicked.connect(equals)

sys.exit(app.exec_())