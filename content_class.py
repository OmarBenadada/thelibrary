import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget,QTextEdit,QMessageBox
from PyQt5.QtGui import QIcon
import pandas as pd



class MainWindow(QWidget):
    
    def __init__(self,thecontent=None):
        super().__init__()
        self.setGeometry(400, 400, 500, 600)
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
        
        Qv=QVBoxLayout()
        
        Qv.addWidget(self.space_for_text)
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
        
        the_text=self.space_for_text.toPlainText()
        if self.thecontent:
            with open(self.thecontent,"w") as file:
                file.write(the_text)
        else:
            QMessageBox.warning(self,"File Error","The .txt file Was not found")
            
            


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
