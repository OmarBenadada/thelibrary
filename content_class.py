import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget,QTextEdit,QMessageBox
from PyQt5.QtGui import QIcon
import pandas as pd



class MainWindow(QWidget):
    
    def __init__(self,thecontent=None):
        super().__init__()
        self.setGeometry(400, 400, 700, 700)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.space_for_text = QTextEdit(self)
        self.SaveButton=QPushButton("Click Here To Save")
        self.thecontent = thecontent
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre","Content"])
        self.Ui()
        
    def Ui(self):
        
        self.QV=QVBoxLayout()
        
        self.space_for_text.setStyleSheet("""
            QTextEdit {
                font-size: 18px;
                color: #2c3e50;
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                padding: 15px;
                line-height: 1.6;
                font-family: 'Segoe UI', sans-serif;
            }
        """)
        
        self.QV.addWidget(self.space_for_text)
        self.space_for_text.setStyleSheet("font-size: 20px ;")
        
        self.SaveButton.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 20px;
                font-weight: bold;
                border-radius: 15px;
                padding: 15px 30px;
                border: 2px solid #2980b9;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            QPushButton:hover {
                background-color: #2980b9;
                border-color: #1c598a;
            }
            QPushButton:pressed {
                background-color: #1c598a;
                border-color: #145374;
            }
        """)
        self.QV.addWidget(self.SaveButton)
        
        self.space_for_text.setStyleSheet("""
            QTextEdit {
                font-size: 18px;
                color: #2c3e50;
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                padding: 15px;
                line-height: 1.6;
                font-family: 'Segoe UI', sans-serif;
            }
        """)
        self.SaveButton.clicked.connect(self.saving)
        self.setLayout(self.QV)
        
    def saving(self):
        
        the_text=self.space_for_text.toPlainText()
        if self.thecontent:
            with open(self.thecontent,"w") as file:
                file.write(the_text)
            QMessageBox.information(self, "Title", "This is an information message.")
        else:
            QMessageBox.warning(self,"File Error","The .txt file Was not found")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
