import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QMessageBox,QLabel,QScrollArea,QFrame
from PyQt5.QtGui import QIcon
import Looking_ForASpecifique_Book
import Looking_for_alot_ofBooks

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.looking_for_Multi=QPushButton("Looking for Multi Books")
        self.looking_for_one=QPushButton("Looking for A Single Book")
        self.Ui()
        self.child_windows = []
        
    def Ui(self):
        QV=QVBoxLayout()
        self.looking_for_Multi.setStyleSheet("""
                    QPushButton {
                        background-color: #0078D7;
                        color: White;
                        font-size: 25px;
                        border-radius: 20px;
                        font-weight: bold;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color:rgb(147, 210, 255);
                        color: white;}""")
        QV.addWidget(self.looking_for_Multi)
        self.looking_for_Multi.clicked.connect(self.multi)
        
        self.looking_for_one.setStyleSheet("""
                    QPushButton {
                        background-color: #0078D7;
                        color: White;
                        font-size: 25px;
                        border-radius: 20px;
                        font-weight: bold;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color:rgb(147, 210, 255);
                        color: white;}""")
        QV.addWidget(self.looking_for_one)
        self.looking_for_one.clicked.connect(self.single)
        
        self.setLayout(QV)
        
    def single(self):
        
        firstwindow=Looking_ForASpecifique_Book.MainWindow()
        self.child_windows.append(firstwindow)
        firstwindow.show()
        
    def multi(self):
        secondwindow=Looking_for_alot_ofBooks.MainWindow()
        self.child_windows.append(secondwindow)
        secondwindow.show()
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    