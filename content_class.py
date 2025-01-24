import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,QLineEdit,QTextEdit
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.space_for_text = QTextEdit(self)
        self.SaveButton=QPushButton("Click Here To Save")
        self.Ui()
        
    def Ui(self):
        
        Qv=QVBoxLayout()
        
        Qv.addWidget(self.space_for_text)
        self.space_for_text.setFixedSize(600, 600)
        self.space_for_text.setStyleSheet("font-size: 20px ;")
        
        self.SaveButton.setStyleSheet("""
            QPushButton {
                background-color:rgba(255, 255, 255, 0.5);
                color: black;
                font-size: 25px;
                border: 2px solid #0078D7;
                border-radius: 20px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color:rgb(147, 210, 255);
                color: white;
            }
        """)
        Qv.addWidget(self.SaveButton)
        self.SaveButton.clicked.connect(self.saving)
        self.setLayout(Qv)
        
    def saving(self):
        pass    


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
