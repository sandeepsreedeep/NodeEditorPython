from PySide2.QtWidgets import QGraphicsEllipseItem
from PySide2.QtGui import QBrush, QPen, QColor
from PySide2.QtCore import Qt
from ui.styles import OUTPUT_PLUG_BORDER, OUTPUT_PLUG, SELECTED_OUTPUT_PLUG_BORDER


class NodeOutput(QGraphicsEllipseItem):
    def __init__(self, attr_name, rect_width, rect_radius, offset_from_rect, parent=None):
        super(NodeOutput, self).__init__(parent)
        self.setBrush(QBrush(QColor(OUTPUT_PLUG)))
        self.default_pen = QPen(OUTPUT_PLUG_BORDER)
        self.selected_pen = QPen(SELECTED_OUTPUT_PLUG_BORDER)
        self._attr_name = attr_name
        self._rect_radius = rect_radius
        self._offset_from_rect = offset_from_rect
        self._rect_width = rect_width
        self.setFlag(QGraphicsEllipseItem.ItemIsSelectable)
        self.setRect(self._rect_width-self._rect_radius, self._offset_from_rect*2.5 + 5, 10, 10)
        self.clicked = False

    @property
    def AttributeName(self):
        return self._attr_name

    @AttributeName.setter
    def AttributeName(self, name):
        self._attr_name = name

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print('lft')
            self.setPen(self.selected_pen)
            self.clicked = True
        super(NodeOutput, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setPen(self.default_pen)
            self.clicked = False
        super(NodeOutput, self).mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if self.clicked:
            print('fsdd')