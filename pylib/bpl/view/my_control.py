# -*- coding: UTF-8 -*-
from PySide2 import QtWidgets, QtCore


class CompleterCombobox(QtWidgets.QComboBox):
    """
    This comboBox supports search and automatically complete
    """
    def __init__(self, *args, **kwargs):
        super(CompleterCombobox, self).__init__(*args, **kwargs)
        # set completer for search
        self.completer = QtWidgets.QCompleter()
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.setEditable(True)
        self.setCompleter(self.completer)

    def set_model(self, list):
        """
        This will set model for the completer
        :param list list: content in model
        :return:
        """
        model = QtCore.QStringListModel()
        model.setStringList(list)
        self.completer.setModel(model)


class TabListWidget(QtWidgets.QListWidget):
    """
    This is a tab QListWidget with normal format
    """
    def __init__(self, *args, **kwargs):
        super(TabListWidget, self).__init__(*args, **kwargs)
        self.setResizeMode(QtWidgets.QListView.Adjust)
        self.setFlow(QtWidgets.QListView.LeftToRight)
        self.setViewMode(QtWidgets.QListView.IconMode)
        self.setMovement(QtWidgets.QListView.Static)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.setGridSize(QtCore.QSize(100, 100))
        self.setIconSize(QtCore.QSize(64, 64))
