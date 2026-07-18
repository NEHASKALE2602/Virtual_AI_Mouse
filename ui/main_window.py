from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget
)

from ui.sidebar import SideBar
from ui.topbar import TopBar
from ui.statusbar import StatusBar

from ui.pages.dashboard_page import DashboardPage
from ui.pages.camera_page import CameraPage
from ui.pages.virtual_mouse_page import VirtualMousePage
from ui.pages.gestures_page import GesturesPage
from ui.pages.settings_page import SettingsPage
from ui.pages.about_page import AboutPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NeuroMouse AI")
        self.resize(1600,900)

        self.setStyleSheet("""
        QMainWindow{
            border:none;
            background:transparent;
        }
        """)

        central = QWidget()

        self.setCentralWidget(central)

        # FULL APPLICATION BACKGROUND
        central.setStyleSheet("""
        QWidget{
            border:none;
            background-image:url(ui/resources/images/hero_bg.jpg);
            background-repeat:no-repeat;
            background-position:center;
        }
        """)

        root = QHBoxLayout(central)

        root.setContentsMargins(20,20,20,20)

        root.setSpacing(20)

        self.sidebar = SideBar()

        root.addWidget(self.sidebar)

        rightWidget = QWidget()

        rightWidget.setStyleSheet("background:transparent;")

        rightLayout = QVBoxLayout(rightWidget)

        rightLayout.setContentsMargins(0,0,0,0)

        rightLayout.setSpacing(20)

        self.topbar = TopBar()

        rightLayout.addWidget(self.topbar)

        self.pages = QStackedWidget()

        self.pages.setStyleSheet("""
        QStackedWidget{
            background:transparent;
        }
        """)

        self.dashboardPage = DashboardPage()
        self.cameraPage = CameraPage()
        self.virtualMousePage = VirtualMousePage()
        self.gesturePage = GesturesPage()
        self.settingsPage = SettingsPage()
        self.aboutPage = AboutPage()

        self.pages.addWidget(self.dashboardPage)
        self.pages.addWidget(self.cameraPage)
        self.pages.addWidget(self.virtualMousePage)
        self.pages.addWidget(self.gesturePage)
        self.pages.addWidget(self.settingsPage)
        self.pages.addWidget(self.aboutPage)

        rightLayout.addWidget(self.pages)

        self.status = StatusBar()

        rightLayout.addWidget(self.status)

        root.addWidget(rightWidget)

        self.sidebar.dashboard.clicked.connect(
            lambda:self.changePage(0,"Dashboard")
        )

        self.sidebar.camera.clicked.connect(
            lambda:self.changePage(1,"Camera")
        )

        self.sidebar.mouse.clicked.connect(
            lambda:self.changePage(2,"Virtual Mouse")
        )

        self.sidebar.gesture.clicked.connect(
            lambda:self.changePage(3,"Gestures")
        )

        self.sidebar.settings.clicked.connect(
            lambda:self.changePage(4,"Settings")
        )

        self.sidebar.about.clicked.connect(
            lambda:self.changePage(5,"About")
        )

    def changePage(self,index,title):

        self.pages.setCurrentIndex(index)

        self.topbar.setTitle(title)