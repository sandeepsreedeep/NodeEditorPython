from PySide2.QtWidgets import QGraphicsItem, QGraphicsItemGroup, QWidget
from PySide2.QtCore import QPointF, QRectF
from ui.NodeRectangle import NodeRectangle
from ui.NodeText import NodeText
from ui.NodeOutput import NodeOutput
from ui.NodeInput import NodeInput


class Node(QGraphicsItemGroup):
    def __init__(self, node_name, pos_x, pos_y, height, width,
                 input_attrs=['in_1', 'in_2'], output_attrs=['out_1'], parent=None):
        super(Node, self).__init__(parent)
        self.setHandlesChildEvents(False)
        self._name = node_name
        self._width = width
        self._height = height
        self._node_rect_radius = 5
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.addToGroup(NodeRectangle(height=height, width=width, radius=self._node_rect_radius))
        self.addToGroup(NodeText(node_name))
        self._input_attrs = input_attrs
        self._output_attrs = output_attrs
        # self.setZValue(-10)
        self._input_plugs = []
        self._output_plugs = []
        self.addInputSockets()
        self.addOutputSockets()
        self.setPos(QPointF(pos_x, pos_y))


    def boundingRect(self):
        super(Node, self).boundingRect()
        penWidth = 1.0
        return QRectF(-penWidth / 2, -penWidth / 2,
                      self._width + penWidth, self._height + penWidth)


    def addOutputSockets(self):
        for attr_index, attr_name in enumerate(self._output_attrs):
            out_plug = NodeOutput(attr_name, rect_width=self._width, rect_radius=self._node_rect_radius, offset_from_rect=attr_index*self._node_rect_radius)
            self._output_plugs.append(out_plug)
            self.addToGroup(out_plug)

    def addInputSockets(self):
        for attr_index, attr_name in enumerate(self._input_attrs):
            in_plug = NodeInput(attr_name, rect_radius=self._node_rect_radius, offset_from_rect=attr_index*self._node_rect_radius)
            self._input_plugs.append(in_plug)
            self.addToGroup(in_plug)

    def paint(self, painter, option, widget):
        return
