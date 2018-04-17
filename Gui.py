#<head>--------------------------------------------------------------------------</head>-#
#@description:RobinJr's personnal GUI interface for GreatWork
#@author:RobinJr.
#@firstedit:2018/4/12
#@lastedit :2018/4/17

#<bug>---------------------------------------------------------------------------</bug>-#
#@bug2018/4/17
#class TrayIcon.quit  bug:self.parent().exit() will not let the application exit
#@debug2018/4/17
#                     substitute by self.parent().close()

#<body>--------------------------------------------------------------------------</body>-#
import sys
import os
# from Module import * get all the 'public' object of Module
from PyQt5.QtWidgets import *               #Widgets: the primary elements for creating user interfaces in Qt.
from PyQt5.QtCore import *              
from PyQt5.QtGui import *

#QsystemTrayIcon 
class TrayIcon(QSystemTrayIcon):
    def __init__(self,parent=None):
        super(TrayIcon,self).__init__(parent)               #super():a function to invoke the parents' method
        self.seticon()
        self.showMenu()
    def showMenu(self):
        # create the main menu for Tray
        self.menu           = QMenu()
        # add the exit action
        self.quitAction     = QAction("exit",self,triggered = self.quit)
         
        self.menu.addAction(self.quitAction)

        self.setContextMenu(self.menu)
    #set the function of exit Action    
    def quit(self):
        self.setVisible(False)
        self.parent().close()
        qApp.quit()
        sys.exit()
    
    def seticon(self):
        # the format of setIcon() must be .ico 
        # !!!: .png file can't be read
        self.setIcon(QIcon("./document/bitbug_favicon.ico"))
        self.icon           = self.MessageIcon()
    def Mshowmassage(self, title ,string):
        # the timehint argument must be 1 , there are some error in this funciton waitting to tackle
        self.showMessage(title,string,self.icon,1)

class window(QWidget):
    def __init__(self,parent=None):
        super(window,self).__init__(parent)
        self.ti = TrayIcon(self)
        self.ti.show()
        self.ti.Mshowmassage("小Z","hello")


#<main>--------------------------------------------------------------------------</main>-#
# a place for test
if __name__ == "__main__":
    # QApplication class manages the GUI application's control flow and main settings
    # sys.argv is a list in Python,which contains the command-line arguments passed to the script
    # especially,sys.arg[0] is the name of the script
    t   = os.system('clear')
    app = QApplication(sys.argv)
    w   = window()
#    w.show()
    sys.exit(app.exec_())
