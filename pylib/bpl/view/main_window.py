# -*- coding: UTF-8 -*-
from PySide2 import QtWidgets as QtWidgets

from .main_mixin import Ui_MainWidget

widgetStyleSheet = u"QWidget { background-color: rgb(67, 67, 67) }"
labelStyleSheet = u"QLabel { border-style:flat;font-weight:500;font-family: Helvetica;color: #BFBFBF;}"
comboBoxStyleSheet = u"QComboBox { border-style:flat;font-weight:300;font-family: Helvetica;color: " \
                     u"#BFBFBF;background-color: #151515;border-radius:3px }"
tabWidgetStyleSheet = u"QTabWidget { border:none;font-weight:500;font-family: Helvetica;color: " \
                     u"#BFBFBF;color: #515151;}"
listWidgetStyleSheet = u"QListWidget { border:none;font-weight:500;font-family: Helvetica;color: " \
                    u"#BFBFBF;background-color: #515151;}"


class MainWindow(QtWidgets.QWidget, Ui_MainWidget):
    """
    Main window of the Dailies tool
    """

    def __init__(self, app, bp_context=None):
        """
        Initializes main window

        :param app: QApplication or QCoreApplication instance of main window
        :param str bp_context: eg ''
        """
        super(MainWindow, self).__init__()
        self.language_dict = {}
        self.language = None
        self.app = app

        # set QSS
        self.app.setStyleSheet(widgetStyleSheet + labelStyleSheet + comboBoxStyleSheet + tabWidgetStyleSheet +
                               listWidgetStyleSheet)

        self.setupUi(self)
        self.setWindowTitle('BPL')
        self.help_button.connect_to_controller(self.controller)

        self.controller.connect_to_main_window(self)
        self.controller.initialize(self.bp_context)
