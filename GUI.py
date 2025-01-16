import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import adding_books_class



class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 600)
        self.setWindowTitle("Virtual Library")
        self.setWindowIcon(QIcon("bookshelf.png"))
        self.initUI()
        self.child_windows = []
        

    def initUI(self):
        label = QLabel("Menu", self)
        label.setFont(QFont("Arial", 28))  
        label.setAlignment(Qt.AlignHCenter )
        label.setStyleSheet("font-weight: bold; color:rgb(29, 25, 25);")

        button_labels = [
            "Adding A Book/s",
            "Looking For A Book/s",
            "Removing a Book/s",
            "Showing The Whole Library",
            "Changing the Data Of A Book/s",
            "Close The Programme ",
        ]

        fonctions = [
            self.Adding_A_Books,
            self.Looking_For_A_Books,
            self.Removing_a_Books,
            self.Showing_The_WholeLibrary,
            self.Changing_the_Data_Of_A_Books,
            self.Close_The_Programme,
        ]

        
        layout = QVBoxLayout()
        layout.addWidget(label)

        for label_text, fonction in zip(button_labels, fonctions):
            button = QPushButton(label_text, self)
            
            button.setFont(QFont("Arial", 10))  
            
            button.setStyleSheet("""
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
            
            button.clicked.connect(fonction)
            
            button.setMinimumHeight(70)
            button.setMaximumHeight(180)
            layout.addWidget(button)

        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    
    def Adding_A_Books(self):
        window = adding_books_class.MainWindow()
        self.child_windows.append(window)  
        window.show()
        

    def Looking_For_A_Books(self):
        print("Displaying data...")

    def Removing_a_Books(self):
        print("Adding student...")

    def Showing_The_WholeLibrary(self):
        print("Searching for student...")

    def Changing_the_Data_Of_A_Books(self):
        print("Calculating general average...")

    def Close_The_Programme(self):
        print("Deleting data...")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
