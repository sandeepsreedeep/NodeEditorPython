from PySide2.QtWidgets import QGraphicsRectItem, QGraphicsItem
from PySide2.QtGui import QBrush, QPen, QColor
from PySide2.QtCore import QRectF, Qt
from ui.styles import RECTANGLE, RECTANGLE_BORDER, SELECTED_RECTANGLE_BORDER


class NodeRectangle(QGraphicsRectItem):
    def __init__(self, height, width, radius, parent=None):
        super(NodeRectangle, self).__init__(parent)
        self._height = height
        self._width = width
        self._radius = radius
        self.setBrush(QBrush(QColor(RECTANGLE)))
        self.default_pen = QPen(RECTANGLE_BORDER)
        self.selected_pen = QPen(SELECTED_RECTANGLE_BORDER)
        # self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.setParentItem(parent)
        self.setHandlesChildEvents(False)

    def boundingRect(self):
        super(NodeRectangle, self).boundingRect()
        penWidth = 1.0
        return QRectF(-penWidth / 2, -penWidth / 2,
                      self._width + penWidth, self._height + penWidth)

    def paint(self, painter, option, widget):
        super(NodeRectangle, self).paint(painter, option, widget)
        painter.setPen(self.selected_pen if self.isSelected() else self.default_pen)
        painter.drawRoundedRect(0, 0, self._width, self._height, self._radius, self._radius)

    def mousePressEvent(self, event):
        print('dfdf')
        super(NodeRectangle, self).mousePressEvent(event)