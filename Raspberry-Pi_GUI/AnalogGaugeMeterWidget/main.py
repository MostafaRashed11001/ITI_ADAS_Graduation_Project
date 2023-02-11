import os
import sys
import random
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication



################################################################################################
# Convert UI to PyQt5 py file
################################################################################################
os.system("pyuic5 -o analoggaugewidget_demo_ui.py analoggaugewidget_demo.ui")
# os.system("pyuic5 -o analoggaugewidget_demo_ui.py analoggaugewidget_demo.ui.oQCkCR")

################################################################################################
# Import the generated UI
################################################################################################
from analoggaugewidget_demo_ui import *

################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.config_button = QtWidgets.QPushButton("Configure", self)
        
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
    
        ################################################################################################
        # Show window
        ################################################################################################
        self.show()

        



########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())

########################################################################
## END===>
########################################################################  