from PySide2.QtWidgets import QMainWindow
from ui.NodeEditor import Ui_MainWindow


class NodeEditorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
