from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget Example")
        
        # Create a button
        self.button = QPushButton("Click Me", self)
        
        # Create a layout to arrange the widgets
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        # Set the layout for the QWidget
        self.setLayout(layout)

def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
