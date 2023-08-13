from PySide2.QtWidgets import QGraphicsRectItem
from PySide2.QtGui import QBrush, QPen, QColor
from PySide2.QtCore import QRectF, Qt
from ui.styles import RECTANGLE, RECTANGLE_BORDER, SELECTED_RECTANGLE_BORDER, RECTANGLE_HEADER


class NodeRectangle(QGraphicsRectItem):
    def __init__(self, height, width, radius, parent=None):
        super(NodeRectangle, self).__init__(parent)
        self._height = height
        self._width = width
        self._radius = radius
        self.default_brush = QBrush(QColor(RECTANGLE))
        self.header_brush = QBrush(QColor(RECTANGLE_HEADER))
        self.setBrush(self.default_brush)
        self.default_pen = QPen(RECTANGLE_BORDER)
        self.default_pen.setWidth(2.0)
        self.selected_pen = QPen(SELECTED_RECTANGLE_BORDER)
        self.selected_pen.setWidth(2.0)
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
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.header_brush)
        painter.drawRoundedRect(0, 2, self._width, self._height/3, self._radius, self._radius)

    def mousePressEvent(self, event):
        print('dfdf')
        super(NodeRectangle, self).mousePressEvent(event)