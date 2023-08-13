
import sys
from PySide2.QtWidgets import QApplication
from ui.NodeEditorWindow import NodeEditorWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NodeEditorWindow()
    window.setWindowTitle("Node Editor")
    window.show()
    sys.exit(app.exec_())