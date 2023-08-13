from PySide2.QtWidgets import QGraphicsEllipseItem
from PySide2.QtGui import QBrush, QPen, QColor
from PySide2.QtCore import QRectF
from ui.styles import INPUT_PLUG, INPUT_PLUG_BORDER, SELECTED_INPUT_PLUG_BORDER


class NodeInput(QGraphicsEllipseItem):
    def __init__(self, attr_name, rect_radius, offset_from_rect, parent=None):
        super(NodeInput, self).__init__(parent)
        self.setBrush(QBrush(QColor(INPUT_PLUG)))
        self.default_pen = QPen(INPUT_PLUG_BORDER)
        self.selected_pen = QPen(SELECTED_INPUT_PLUG_BORDER)
        self._attr_name = attr_name
        self._rect_radius = rect_radius
        self._offset_from_rect = offset_from_rect
        # self.setZValue(100)
        self.setRect(-self._rect_radius, self._offset_from_rect*2.5 + 5, 10, 10)
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)

    @property
    def AttributeName(self):
        return self._attr_name

    @AttributeName.setter
    def AttributeName(self, name):
        self._attr_name = name


    def mousePressEvent(self, event):
        print('clicked')
        self.setPen(self.selected_pen)
        super(NodeInput, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        print('released')
        self.setPen(self.default_pen)
        super(NodeInput, self).mouseReleaseEvent(event)

