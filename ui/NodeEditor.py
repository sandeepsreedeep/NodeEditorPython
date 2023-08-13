# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NodeEditor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui.EditorBG import EditorBG
from ui.Node import Node
from ui.EditorView import EditorView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bg = EditorBG()
        self.graphicsView = EditorView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setScene(self.bg)

        self.verticalLayout.addWidget(self.graphicsView)
        nodes = ['node_1', 'node_2', 'node_3']
        for node_index, node in enumerate(nodes):
            self.bg.addItem(Node(node_name=node, pos_x=node_index*70, pos_y=node_index*100, height=50, width=80))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *
# from ui.EditorBG import EditorBG
# from ui.Node import Node
# from ui.NodeContainer import NodeContainer
# from ui.EditorView import EditorView
#
#
# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         if not MainWindow.objectName():
#             MainWindow.setObjectName(u"mainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QWidget(MainWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.verticalLayout = QVBoxLayout(self.centralwidget)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.bg = EditorBG()
#         self.graphicsView = EditorView(self.centralwidget)
#         self.graphicsView.setObjectName(u"graphicsView")
#         # self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         # self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
#         self.graphicsView.setScene(self.bg)
#         nodes = ['node_1', 'node_2', 'node_3']
#         # for node_index, node in enumerate(nodes):
#         # _node = NodeContainer(scene=self.bg,node_name='node_1', pos_x=0*70, pos_y=0*100, height=50, width=80)
#
#         self.verticalLayout.addWidget(self.graphicsView)
#
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(MainWindow)
#         self.menubar.setObjectName(u"menubar")
#         self.menubar.setGeometry(QRect(0, 0, 800, 21))
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(MainWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(MainWindow)
#
#         QMetaObject.connectSlotsByName(MainWindow)
#     # setupUi
#
#     def retranslateUi(self, MainWindow):
#         MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#     # retranslateUi
#
