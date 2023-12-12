# gui.py
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QTextEdit, QMessageBox
from grades import get_grade

class GradeCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Grade Calculator")

        # Number of students entry
        self.num_students_label = QLabel("Total number of students:")
        self.num_students_entry = QLineEdit()

        # Scores entry
        self.scores_label = QLabel("Enter scores separated by spaces:")
        self.scores_entry = QLineEdit()

        # Calculate button
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate_grade)

        # Result text
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.num_students_label)
        layout.addWidget(self.num_students_entry)
        layout.addWidget(self.scores_label)
        layout.addWidget(self.scores_entry)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def calculate_grade(self):
        try:
            num_students = int(self.num_students_entry.text())

            if num_students <= 0:
                QMessageBox.warning(self, "Invalid Input", "Please enter a valid number of students.")
                return

            scores_input = self.scores_entry.text().split()

            if len(scores_input) != num_students:
                QMessageBox.warning(self, "Invalid Input", f"Please enter {num_students} score(s).")
                return

            scores = [int(score) for score in scores_input]
            all_scores = scores[:]  # create a copy for calculating grades

            total_score = sum(scores)
            self.result_text.clear()  # Clear previous results

            for i, score in enumerate(scores):
                grade = get_grade(score, all_scores)
                self.result_text.insertPlainText(f"Student {i + 1} score is {score} and grade is {grade}\n")

            average_score = total_score / num_students
            average_grade = get_grade(average_score, all_scores)
            self.result_text.insertPlainText(f"\nThe average score is {average_score:.2f}, a grade of {average_grade}")

        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid scores separated by spaces.")


if __name__ == "__main__":
    app = QApplication([])
    window = GradeCalculatorApp()
    window.show()
    app.exec()
