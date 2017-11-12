from PyQt4 import QtGui # Import the PyQt4 module we'll need
import sys # We need sys so that we can pass argv to QApplication

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#import app as app_design  # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

import manager, setup, brewer


import matplotlib.pyplot as plt
class MakeChart(object):
    def __init__(self):
        temps = [10, 5, 9, 4, 10, 8, 6, 8, 6, 7, 4, 8, 5, 9, 8, 7, 5, 5, 7, 5, 8, 6, 8, 7, 7, 5, 5, 6, 8, 8, 9, 6, 9]

        def average(grades):
            return sum(grades)/len(grades)

        def generate_average(grades):
            out = []
            for period in range(1, len(grades)+1):
                out.append(average(grades[0:period]))
            return out

        plt.ion()
        plt.plot(generate_average(temps))
        plt.pause(0.001)
        plt.ylabel('Temperature')
        plt.xlabel('Time')
        plt.grid()
        
        plt.pause(0.001)
        plt.show(block=True)




class Manager(QtGui.QMainWindow, manager.Ui_Dialog):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

    def accept(self):
        pass

    def reject(self):
        pass

class SetUp(QtGui.QMainWindow, setup.Ui_Dialog):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

    def accept(self):
        pass

    def reject(self):
        pass

class Brewer(QtGui.QMainWindow, brewer.Ui_Dialog):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined

        self.label_22.setPixmap(QPixmap("assets/tank.jpg"))
        self.label_23.setPixmap(QPixmap("assets/tank.jpg"))
        self.label_24.setPixmap(QPixmap("assets/tank.jpg"))
        self.label_25.setPixmap(QPixmap("assets/tank.jpg"))
        
        self.timer_count = 0 

        self.pushButton.clicked.connect(self.open_manage)
        self.pushButton_2.clicked.connect(lambda: MakeChart())

        def tick():
            self.timer_count +=1
            self.update_progress_bars(self.timer_count)
            print 'tick', self.timer_count



        self.timer = QTimer()
        self.timer.timeout.connect(tick)
        self.timer.start(1000)

        self.manager = Manager()

    def open_manage(self):
        self.manager.show()

    def update_progress_bars(self, time):
        # update once every 3 seconds
        if time%3 == 0:
            # everything is bounded to 100%
            self.process_progress.setValue(self.process_progress.value()+1 if self.process_progress.value()+1 < 100 else 100)
            self.process_progress_2.setValue(self.process_progress_2.value()+1 if self.process_progress_2.value()+1 < 100 else 100)
            self.process_progress_3.setValue(self.process_progress_3.value()+1 if self.process_progress_3.value()+1 < 100 else 100)
            self.process_progress_4.setValue(self.process_progress_4.value()+1 if self.process_progress_4.value()+1 < 100 else 100)

    def accept(self):
        pass

    def reject(self):
        pass

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
                     # We set the form to be our ExampleApp (design)
                             # Show the form

    setup = SetUp()
    setup.show()

    brewer = Brewer()
    brewer.show()

    
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function