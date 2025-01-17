import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QListWidget,QMessageBox
from PyQt5.QtGui import QIcon
import books
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,700,700)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.vbox=QVBoxLayout()
        
        self.book_list = QListWidget()
        self.vbox.addWidget(self.book_list)
        
        self.data_info={}
        self.Labels_infos()
        
        self.add=QPushButton("Add")
        self.vbox.addWidget(self.add)
        self.add.clicked.connect(self.on_click_add)
        
        self.remove=QPushButton("Remove")
        self.vbox.addWidget(self.remove)
        self.remove.clicked.connect(self.on_click_remove)
        
        self.edit=QPushButton("Edit")
        self.vbox.addWidget(self.edit)
        self.edit.clicked.connect(self.on_click_edit)
 
        self.Buttons()

    def Labels_infos(self):   
        
        names=['Title','Author','Year','Genre']
        for name in names:
            field=QLineEdit(self)
            field.setPlaceholderText(f"Enter the {name} ...")
            field.setStyleSheet("font-size:20px; ")
            self.vbox.addWidget(field)
            self.data_info[name]=field
        self.setLayout(self.vbox)  
        return self.data_info 
    
    def Buttons(self):    
        buttons=[self.add,self.remove,self.edit]
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
                        background-color:rgb(147, 210, 255);
                        color: white;}""")
    
    # def on_click(self):
        
    #     title=self.data_info['Title'].text()
    #     author=self.data_info['Author'].text()
    #     year=self.data_info['Year'].text()
    #     genre=self.data_info['Genre'].text()
        
    #     if not year.isdigit():
    #         print("Year must be a valid number.")
    #         return

    #     try:
    #         df = pd.read_csv("thelibraryy.csv")
    #     except FileNotFoundError:
    #         df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
        
    #     if not df[(df["Title"]==title) & (df["Author"]==author)].empty:
    #         print(f"this book {author} already Exist in the library ")
            
   
    #     else:
    #         book = books.Books(title=title, author=author, year=year, genre=genre)
    #         frame = pd.DataFrame([{"Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre}])
            
    #         df=pd.concat([df,frame],axis=0,ignore_index=True)
            
    #         df.to_csv("thelibraryy.csv", index=False)
            
    #         print("book is added to the library")
    def on_click_add(self):
        
            title=self.data_info['Title'].text()
            author=self.data_info['Author'].text()
            year=self.data_info['Year'].text()
            genre=self.data_info['Genre'].text()
            
            try:
                df = pd.read_csv("thelibraryy.csv")
            except FileNotFoundError:
                df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])
            if not year.isdigit():
                QMessageBox.warning(self,"Input Error",f"Year Must Be A number not {year}")
                return    
            if (title and author and year and genre):   
                if not df[(df["Title"]==title) & (df["Author"]==author)].empty:
                    QMessageBox.warning(self,"Input Error",f"this book {author} already Exist in the library ")
                else:
                    book = books.Books(title=title, author=author, year=year, genre=genre)
                    frame = pd.DataFrame([{"Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre}])
                    
                    df=pd.concat([df,frame],axis=0,ignore_index=True)
                    
                    df.to_csv("thelibraryy.csv", index=False)
                    self.book_list.addItem(f'the book {{{title}}} by {{{author}}} written in {{{year}}} and its {{{genre}}}')
                    print("book is added to the library")
            else:
                QMessageBox.warning(self,"Input Error","You Forgot to Fill A Label")            
                
                
                
            
    def on_click_remove(self):
            pass
    def on_click_edit(self):
            pass
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
