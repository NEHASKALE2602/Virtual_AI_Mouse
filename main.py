import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow


def load_theme(app):
    try:
        with open("ui/themes/dark.qss", "r", encoding="utf-8") as file:
            app.setStyleSheet(file.read())
            print("Theme Loaded Successfully")
    except Exception as e:
        print("Theme Loading Error:", e)


def main():

    app = QApplication(sys.argv)

    load_theme(app)

    window = MainWindow()

    window.showMaximized()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()