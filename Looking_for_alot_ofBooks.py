import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QMessageBox,QLabel,QScrollArea
from PyQt5.QtGui import QIcon
import books
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.search_button=QPushButton("Search")
        self.title_label=QLineEdit("Enter the Title...",self)
        self.Ui()
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])

        
    def Ui(self):
        
        self.QV=QVBoxLayout()
        
        self.search_button.setStyleSheet("""
                    QPushButton {
                        background-color: #0078D7;
                        color: White;
                        font-size: 15px;
                        border-radius: 20px;
                        font-weight: bold;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color:rgb(147, 210, 255);
                        color: white;}""")
        self.QV.addWidget(self.search_button)
        
        self.title_label.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                padding: 10px;
                border: 2px solid #0078D7;
                border-radius: 10px;
            }
        """)
        self.QV.addWidget(self.title_label)
        self.setLayout(self.QV)
        
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background: #f7f7f7; border: none;")
        self.result_box=QWidget()
        self.QV_result_box=QVBoxLayout(self.result_box)
        self.QV.addWidget(self.scroll_area)
            
        
        
        
        
        
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
