from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


def main() -> None:
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Top"))
    layout.addWidget(QPushButton("Bottom"))
    window.setLayout(layout)
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
