import sys
from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QPushButton,QHBoxLayout,QLabel,QVBoxLayout,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

import pandas as pd

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400,400,600,250)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.search=QPushButton("Click Here To Search")
        self.field=QLineEdit(self)
        self.field.setPlaceholderText(f"Enter the Year ...")
        self.theauthor = ""
        self.the_number=None
        self.theone=None
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
        # Get the year input and strip extra spaces
        self.theyear = self.field.text().strip()

        try:
            # Load the CSV file
            df = pd.read_csv("thelibraryy.csv")
        except FileNotFoundError:
            # Create an empty DataFrame if the file doesn't exist
            df = pd.DataFrame(columns=["Title", "Author", "Year", "Genre"])

        # Clear old results (remove widgets from the layout)
        while self.main_vbox.count() > 1:  
            item = self.main_vbox.takeAt(1)
            if item.widget():
                item.widget().deleteLater()

        # Check if the input is empty
        if not self.theyear:
            QMessageBox.warning(self, "Input Error", "You didn't write anything.")
            return

        # Filter the DataFrame for matching rows
        self.theone = df[df["Year"].astype(str) == self.theyear]
        self.the_number = self.theone.shape[0]

        # If no results are found
        if self.theone.empty:
            QMessageBox.warning(self, "Search Result", "Nothing was found.")
        else:
            # Display results
            for _, content in self.theone.iterrows():
                # Create a horizontal layout for each result
                row_layout = QHBoxLayout()

                # Create a label with the book details
                label = QLabel(self)
                label.setText(
                    f"Title: {content['Title']} | "
                    f"Author: {content['Author']} | "
                    f"Year: {content['Year']} | "
                    f"Genre: {content['Genre']}"
                )
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet("font-size:20px;")

                # Add the label to the horizontal layout
                row_layout.addWidget(label)

                # Add the horizontal layout to the main vertical layout
                self.main_vbox.addLayout(row_layout)

                
   
      
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
