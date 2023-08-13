from PySide2.QtWidgets import QGraphicsView
from PySide2.QtWidgets import QGraphicsSceneMouseEvent
from PySide2.QtGui import QMouseEvent, QPainter
from PySide2.QtCore import Qt


class EditorView(QGraphicsView):
    def __init__(self, parent=None):
        super(EditorView, self).__init__(parent)
        self.zoom = 10
        self.zoomInFactor = 1.25
        self.zoomStep = 1
        self.zoomRange = [0, 10]
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing
                            | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonPressEvent(event)
        else:
            super(EditorView, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.button() == Qt.MiddleButton:
            self.middleMouseButtonReleaseEvent(event)
        else:
            super(EditorView, self).mouseReleaseEvent(event)

    def middleMouseButtonPressEvent(self, event) -> None:
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        fake_event = QMouseEvent(event.type(), event.localPos(), Qt.LeftButton, event.buttons(), event.modifiers())
        super(EditorView, self).mousePressEvent(fake_event)

    def middleMouseButtonReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.setDragMode(QGraphicsView.DragMode.NoDrag)
        fake_event = QMouseEvent(event.type(), event.localPos(), Qt.LeftButton, event.buttons(), event.modifiers())
        super(EditorView, self).mouseReleaseEvent(fake_event)
        pass

    def wheelEvent(self, event) -> None:
        zoomOutFactor = 1/self.zoomInFactor

        if event.delta()>0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep
        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep

        self.scale(zoomFactor, zoomFactor)
        super(EditorView, self).wheelEvent(event)

