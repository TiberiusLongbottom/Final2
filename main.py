# main.py
from gui import GradeCalculatorApp
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    window = GradeCalculatorApp()
    window.show()
    app.exec()
