# -*- coding: UTF-8 -*-
import sys
import os
import logging
import PySide2.QtWidgets as QtWidgets

from bpl.view.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)

    main_window = MainWindow(app)
    main_window.show()

    app.exec_()


if __name__ == '__main__':
    logging.basicConfig()
    main()
