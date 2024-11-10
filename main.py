from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import random

app = QApplication([])
ex = QMainWindow()


ui = Ui_MainWindow()
ui.setupUi(ex)

def generate():
    letters = "qwertyuiopasdfghjklzxcvbnm"
    numbers = "1234567890"
    password_length = 10
    password_list = []
    for i in range(password_length):
        if ui.useleters.isChecked():
            random_letter = random.choice(letters)
            password_list.append(random_letter)
        if ui.usenumbers.isChecked():
            random_number = random.choice(numbers)
            password_list.append(random_number)

    password_str = "".join(password_list)
    ui.result.setText(password_str)

ui.pushButton.clicked.connect(generate)

ex.show()
app.exec()