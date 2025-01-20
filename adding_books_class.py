import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QVBoxLayout,QWidget,QPushButton,QListWidget,QMessageBox
from PyQt5.QtGui import QIcon
import books
import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.vbox=QVBoxLayout()
        
        try:
            self.df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            self.df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])

        i=0
        listo=[]
        while self.df.shape[0]>i:
            listo.append(f'the book  {{{self.df["Title"][i]}}}  by  {{{self.df["Author"][i]}}}  written in  {{{self.df["Year"][i]}}}  and its  {{{self.df["Genre"][i]}}}')
            i+=1    
        
        self.book_list = QListWidget()
        self.vbox.addWidget(self.book_list)
        self.book_list.setStyleSheet("font-size:20px ;")
        self.book_list.addItems(listo)
        
        self.result=None
        
        self.data_info={}
        self.Labels()
        
        self.title=self.data_info['Title'].text()
        self.author=self.data_info['Author'].text()
        self.year=self.data_info['Year'].text()
        self.genre=self.data_info['Genre'].text()
        
        
        self.Buttons()

    def Labels(self):   
        
        self.names=['Title','Author','Year','Genre']
        for name in self.names:
            self.field=QLineEdit(self)
            self.field.setPlaceholderText(f"Enter the {name} ...")
            self.field.setStyleSheet("font-size:20px; ")
            self.vbox.addWidget(self.field)
            self.data_info[name]=self.field
        self.setLayout(self.vbox)  
        
        return self.data_info 
        
    def Buttons(self):
        
        self.add=QPushButton("Add")
        self.vbox.addWidget(self.add)
        self.add.clicked.connect(self.on_click_add)
        
        self.remove=QPushButton("Remove")
        self.vbox.addWidget(self.remove)
        self.remove.clicked.connect(self.on_click_remove)
        
        self.edit=QPushButton("Edit")
        self.vbox.addWidget(self.edit)
        self.edit.clicked.connect(self.on_click_edit)
            
        buttons=[self.add,self.remove,self.edit]
        for i in buttons:
            i.setStyleSheet("""
                    QPushButton {
                        background-color:rgba(255, 255, 255, 0.5);
                        color: black;
                        font-size: 15px;
                        border: 2px solid #0078D7;
                        border-radius: 20px;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color:rgb(147, 210, 255);
                        color: white;}""")
    
    def on_click_add(self):
        self.title = self.data_info['Title'].text()
        self.author = self.data_info['Author'].text()
        self.year = self.data_info['Year'].text()
        self.genre = self.data_info['Genre'].text()

        if not self.year.isdigit():
            QMessageBox.warning(self,"Input Error",f"Year Must Be A number not {self.year}")
            return 
           
        if (self.title and self.author and self.year and self.genre):   
            
            if not self.df[(self.df["Title"]==self.title) & (self.df["Author"]==self.author)].empty:
                QMessageBox.warning(self,"Input Error",f"this book {self.author} already Exist in the library ")
            else:
                book = books.Books(title=self.title, author=self.author, year=self.year, genre=self.genre)
                frame = pd.DataFrame([{"Title": book.title, "Author": book.author, "Year": book.year, "Genre": book.genre}])   
                self.df=pd.concat([self.df,frame],axis=0,ignore_index=True)   
                self.df.to_csv("thelibraryy.csv", index=False)
                self.book_list.addItem(f'the book  {{{self.title}}}  by  {{{self.author}}}  written in  {{{self.year}}}  and its  {{{self.genre}}}')
                print("book is added to the library")
                for names,labels in self.data_info.items():
                    labels.setText("")
        else:
                QMessageBox.warning(self,"Input Error","You Forgot to Fill a Label") 
                             
                             
    def on_click_remove(self):
        
        selected_item=self.book_list.currentItem()
        if selected_item:
            item_text=selected_item.text()
            start_oftitle=item_text.find("{")+1
            end_oftitle=item_text.find("}")
            self.result=item_text[start_oftitle:end_oftitle]
            self.df=self.df[~(self.df['Title']==self.result)]
            self.df.to_csv("thelibraryy.csv", index=False)
            self.book_list.takeItem(self.book_list.row(selected_item))
        else:
            QMessageBox.warning(self,"Selection Error","You Didn't Select Any Row")
                
                
    def on_click_edit(self):
        selected_item=self.book_list.currentItem()
        if selected_item:
            self.book_list.takeItem(self.book_list.row(selected_item))
            self.df=self.df[~(self.df['Title']==self.result)]

            item_text = selected_item.text()
            
            start_of_title = item_text.find("{") + 1
            end_of_title = item_text.find("}")
            title = item_text[start_of_title:end_of_title]
            
            start_of_author = item_text.find("by") + 5
            end_of_author = item_text.find("written")-3
            author = item_text[start_of_author:end_of_author]

            start_of_year = item_text.find("written in") + 13
            end_of_year = item_text.find("and its")-3
            year = item_text[start_of_year:end_of_year]

            start_of_genre = item_text.find("its") + 6
            genre = item_text[start_of_genre:-1]
            items={'Title':title,"Author":author,"Year":year,"Genre":genre}
            for names,labels in self.data_info.items():
                labels.setText(items[names])
        else: 
            QMessageBox.warning(self,"Selection Error","You Didn't Select Any Row")       
            
            
            
            
    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
