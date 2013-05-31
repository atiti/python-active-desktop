#!/usr/bin/python
# 
# By Attila Sukosd (attila@cc.dtu.dk)
# Licensed under BSD
# (C) 2013
# 
#
# usage: activedesktop.py [-h] [-f FULLSCREEN] URL
#
# positional arguments:
#  URL                   The URL to display in the Active Desktop
#
# optional arguments:
#  -h, --help            show this help message and exit
#  -f FULLSCREEN, --fullscreen FULLSCREEN
#                        Launch the desktop in full screen
#

import sys, webbrowser, argparse
from PyQt4 import QtCore, QtGui, QtWebKit
from PyQt4.QtCore import *

class ActiveDesktopClass(QtCore.QObject):
    """Simple Active Desktop class"""

    @QtCore.pyqtSlot(str)
    def launchBrowser(self, url):
        """Open a browser"""
	print "Opening a browser with url:",url
	webbrowser.open_new(url)

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("URL", help="The URL to display in the Active Desktop")
    parser.add_argument("-f", "--fullscreen", help="Launch the desktop in full screen", type=int, default=0)
    args = parser.parse_args()

    URL = args.URL

    app = QtGui.QApplication([])
    activeDesktop = ActiveDesktopClass()

    webView = QtWebKit.QWebView()
    # Make activeDesktop exposed as JavaScript object named 'activeDesktop'
    webView.page().mainFrame().addToJavaScriptWindowObject("activeDesktop", activeDesktop)
    webView.page().mainFrame().load(QUrl(URL))
    # Disable scrollbars
    webView.page().mainFrame().setScrollBarPolicy(Qt.Vertical, Qt.ScrollBarAlwaysOff)
    webView.page().mainFrame().setScrollBarPolicy(Qt.Horizontal, Qt.ScrollBarAlwaysOff)

    window = QtGui.QMainWindow()
    window.setCentralWidget(webView)
    window.setWindowTitle("Active Desktop")
    
    if args.fullscreen == 1:
    	window.showFullScreen()
    else:
        window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

