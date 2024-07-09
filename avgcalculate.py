import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont

class GradeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.addButton = QPushButton('افزودن درس')
        self.addButton.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px; padding: 10px;")
        self.addButton.clicked.connect(self.addCourseRow)
        self.layout.addWidget(self.addButton)

        self.calculateButton = QPushButton('محاسبه معدل')
        self.calculateButton.setStyleSheet("background-color: #2196F3; color: white; font-size: 16px; padding: 10px;")
        self.calculateButton.clicked.connect(self.calculateGPA)
        self.layout.addWidget(self.calculateButton)

        self.setLayout(self.layout)
        self.setWindowTitle('محاسبه معدل')
        self.setStyleSheet("background-color: #f0f0f0;")
        self.show()

    def addCourseRow(self):
        rowLayout = QHBoxLayout()
        
        courseName = QLineEdit()
        courseName.setPlaceholderText('نام درس')
        courseName.setFont(QFont('Arial', 14))
        rowLayout.addWidget(courseName)
        
        courseGrade = QLineEdit()
        courseGrade.setPlaceholderText('نمره')
        courseGrade.setFont(QFont('Arial', 14))
        rowLayout.addWidget(courseGrade)
        
        courseCredits = QLineEdit()
        courseCredits.setPlaceholderText('واحد')
        courseCredits.setFont(QFont('Arial', 14))
        rowLayout.addWidget(courseCredits)
        
        rowLayout.setSpacing(10)
        self.layout.addLayout(rowLayout)

    def calculateGPA(self):
        totalCredits = 0
        totalPoints = 0
        for i in range(self.layout.count() - 2):  # Skip the first two buttons
            rowLayout = self.layout.itemAt(i + 2).layout()
            courseGrade = float(rowLayout.itemAt(1).widget().text())
            courseCredits = float(rowLayout.itemAt(2).widget().text())
            totalCredits += courseCredits
            totalPoints += courseGrade * courseCredits
        
        if totalCredits > 0:
            gpa = totalPoints / totalCredits
            self.showGPA(gpa)
        else:
            self.showGPA(0)

    def showGPA(self, gpa):
        gpaLabel = QLabel(f'معدل: {gpa:.2f}')
        gpaLabel.setFont(QFont('Arial', 16))
        gpaLabel.setStyleSheet("color: #333; padding: 10px;")
        self.layout.addWidget(gpaLabel)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GradeCalculator()
    sys.exit(app.exec_())