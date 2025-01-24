import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
import adding_books_class
import classe_for_the_looking_button



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
            "Manipulating Data/s",
            "Looking For info of Book/s",
            "Showing The Whole Library",
            "Content",
            "Close The Programme ",
        ]

        fonctions = [
            self.Manipulating_Data,
            self.Looking_Forinfo_of_Books,
            self.Showing_The_WholeLibrary,
            self.Content,
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

                        border-radius: 20px;
                        padding: 10px;
                    }
                    QPushButton:hover {
                        background-color:rgb(21, 0, 255);
                        color: white;}""")
            
            button.clicked.connect(fonction)
            
            button.setMinimumHeight(70)
            button.setMaximumHeight(180)
            layout.addWidget(button)

        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    
    def Manipulating_Data(self):
        window = adding_books_class.MainWindow()
        self.child_windows.append(window)  
        window.show()
        

    def Looking_Forinfo_of_Books(self):
        looking_window=classe_for_the_looking_button.MainWindow()
        self.child_windows.append(looking_window)
        looking_window.show()

    def Showing_The_WholeLibrary(self):
        print("Searching for student...")

    def Close_The_Programme(self):
        sys.exit()
        
    def Content(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
