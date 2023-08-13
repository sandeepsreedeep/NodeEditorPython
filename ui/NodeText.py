from PySide2.QtWidgets import QGraphicsItem, QGraphicsSimpleTextItem
from PySide2.QtGui import QPen
from PySide2.QtCore import Qt, QPointF
from ui.styles import TEXT_COLOR, TEXT_SELECTED_COLOR


class NodeText(QGraphicsSimpleTextItem):
    def __init__(self, title="My_Node", parent=None):
        super(NodeText, self).__init__(parent)
        self._title = title
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.default_pen = QPen(TEXT_COLOR)
        self.default_pen.setWidth(10)
        self.selected_pen = QPen(TEXT_SELECTED_COLOR)
        self.selected_pen.setWidth(10)

    def paint(self, painter, option, widget):
        super(NodeText, self).paint(painter, option, widget)
        painter.setPen(self.selected_pen if self.isSelected() else self.default_pen)
        painter.drawText(QPointF(10, 12), self._title)
