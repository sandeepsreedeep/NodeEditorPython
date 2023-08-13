from PySide2.QtWidgets import QGraphicsItem, QGraphicsSimpleTextItem
from PySide2.QtGui import QPen
from PySide2.QtCore import Qt, QPointF


class NodeText(QGraphicsSimpleTextItem):
    def __init__(self, title="My_Node", parent=None):
        super(NodeText, self).__init__(parent)
        self._title = title
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.default_pen = QPen(Qt.black, 5)
        self.selected_pen = QPen(Qt.green)

    def paint(self, painter, option, widget):
        super(NodeText, self).paint(painter, option, widget)
        painter.setPen(self.selected_pen if self.isSelected() else self.default_pen)
        painter.drawText(QPointF(0, -10), self._title)
