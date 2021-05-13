from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


def main() -> None:
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
