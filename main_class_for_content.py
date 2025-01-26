import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QListWidget,QMessageBox
from PyQt5.QtGui import QIcon
import books
import pandas as pd
import content_class


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 800)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.vbox=QVBoxLayout()
        self.child_classes=[]
        self.thecontent=None
        
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre", "Content","ID"])
        self.qlist()
        self.Buttons()
        
    
    def Buttons(self):
        
        self.insert=QPushButton("Insert Content")
        self.vbox.addWidget(self.insert)
        self.insert.clicked.connect(self.inserte)
        
        self.read=QPushButton("Read Content")
        self.vbox.addWidget(self.read)
        
        buttons=[self.insert,self.read]
        for i in buttons:
            i.setStyleSheet("""
                    QPushButton {
                        background-color:rgba(255, 255, 255, 0.5);
                        color: black;
                        font-size: 25px;
                        border: 2px solid #0078D7;
                        border-radius: 20px;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color:rgb(0, 170, 255);
                        color: white;}""")
        self.setLayout(self.vbox)
        
    def qlist(self):
        i = 0
        listo = []
        while self.df.shape[0] > i:
            listo.append(f'ID: {self.df["ID"][i]} - the book  {{{self.df["Title"][i]}}}  by  {{{self.df["Author"][i]}}}  written in  {{{self.df["Year"][i]}}}  and its  {{{self.df["Genre"][i]}}}')
            i += 1
        
        book_list = QListWidget()
        self.vbox.addWidget(book_list)
        book_list.setStyleSheet("font-size:20px ;")
        book_list.addItems(listo)
        book_list.itemClicked.connect(self.exctractor)
        
    def exctractor(self,item_text):
        
        self.selected_text = item_text.text()
        start = self.selected_text .find("{") + 1
        end = self.selected_text .find("}")
        thetitle=self.selected_text [start:end]
        
        theone=self.df[self.df["Title"]==thetitle].iloc[0]
        self.thecontent=theone["Content"]

    def inserte(self):

        if self.selected_text:
            insertion = content_class.MainWindow(thecontent=self.thecontent)
            self.child_classes.append(insertion)
            insertion.show()
        else:
            QMessageBox.warning(self, "Selection Error", "No item selected!")
                
        
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
