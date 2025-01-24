import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,QScrollArea,QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre","Content"])
        self.Ui()
        
    def Ui(self):
        
        the_big_scroll_area=QScrollArea()
        the_big_scroll_area.setWidgetResizable(True)
        
        book_container=QWidget()
        the_big_scroll_area.setWidget(book_container)
        
        small_book_container=QGridLayout()
        book_container.setLayout(small_book_container)
        
        
        for i,books in self.df.iterrows():
            labels=QLabel(f'{books["Title"]}')
            labels.setFont(QFont("Arial", 14))
            labels.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 5px; padding: 10px;")
            labels.setAlignment(Qt.AlignCenter)
            small_book_container.addWidget(labels,i//3,i%3)
            
        QV=QVBoxLayout()
        QV.addWidget(the_big_scroll_area)
        self.setLayout(QV)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
