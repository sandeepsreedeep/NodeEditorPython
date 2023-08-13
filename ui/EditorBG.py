from PySide2.QtWidgets import QGraphicsScene
from PySide2.QtGui import QBrush, QPen
from PySide2.QtCore import Qt, QLine
from ui.styles import DARK_GRID_LINES, LIGHT_GRID_LINES


class EditorBG(QGraphicsScene):
    def __init__(self, parent=None):
        super(EditorBG, self).__init__(parent)
        self.setBackgroundBrush(QBrush(Qt.darkGray))
        self.pen = QPen(LIGHT_GRID_LINES)
        self.dark_pen = QPen(DARK_GRID_LINES)
        # self.setSceneRect(0,0,4000,4000)

    def drawBackground(self, painter, rect) -> None:
        super(EditorBG, self).drawBackground(painter, rect)
        lines = []
        dark_lines = []
        for cnt, x in enumerate(range(int(rect.left()), int(rect.right()), 5)):
            line = QLine(x, int(rect.top()), x, int(rect.bottom()))
            if cnt % 5 == 0:
                dark_lines.append(line)
            else:
                lines.append(line)
        for cnt, y in enumerate(range(int(rect.top()), int(rect.bottom()), 5)):
            line = QLine(int(rect.left()), y, int(rect.right()), y)
            if cnt % 5 == 0:
                dark_lines.append(line)
            else:
                lines.append(line)

        painter.setPen(self.pen)
        painter.drawLines(lines)
        painter.setPen(self.dark_pen)
        painter.drawLines(dark_lines)




