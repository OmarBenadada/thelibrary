import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QPushButton,QHBoxLayout,QLabel,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,500,350)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.search=QPushButton("Click Here To Search")
        self.field=QLineEdit(self)
        self.field.setPlaceholderText(f"Enter the Title ...")
        self.thetitle = ""
        self.data_info = self.Ui()

    def Ui(self):
        
        self.main_vbox = QVBoxLayout()
        
        self.QH=QHBoxLayout()
        self.QH.setAlignment(Qt.AlignTop)
        
        self.search.setStyleSheet("""
                                    QPushButton {
                                        background-color:rgba(255, 255, 255, 0.5);
                                        color: black;
                                        font-size: 20px;
                                        border: 2px solid #0078D7;
                                        border-radius: 20px;
                                        padding: 10px;
                                    }
                                    QPushButton:hover {
                                        background-color:rgb(147, 210, 255);
                                        color: white;
                                    }
                                """)
        
        self.search.clicked.connect(self.on_click) 
        
        
        
        self.field.setStyleSheet("font-size:30px; ")
        
        
        self.QH.addWidget(self.field)
        
            
        self.QH.addWidget(self.search)    
        self.main_vbox.addLayout(self.QH)
        self.setLayout(self.main_vbox)
        
    
    def on_click(self):
        self.thetitle=self.field.text()
        try:
            df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])    
        
        theone = df[(df["Title"] == self.thetitle)]
        
        if theone.empty: 
            label=QLabel(f"""Title: Not found  
        
Author: Not found 
                               
Year: Not found 
                              
Genre: Not found """,self)
            label.setObjectName('label_nember_zero')
            self.main_vbox.addWidget(label)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("font-size:30px; ")
            
        else:
            row_layout=QHBoxLayout()
            for rows_ind,content in theone.iterrows():
                label=QLabel(self)
                label.setText(f"""Title       {content["Title"]}
Author      {content["Author"]}
Year        {content["Year"]}
Genre     {content["Genre"]}""")
                label.setObjectName(f"label_number_{rows_ind}")
                row_layout.addWidget(label)
                self.main_vbox.addLayout(row_layout)
                label.setStyleSheet("font-size:30px;")
                
   
      
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
