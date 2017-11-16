import random
import sys  # We need sys so that we can pass argv to QApplication

import matplotlib.pyplot as plt
from PyQt4 import QtGui  # Import the PyQt4 module we'll need
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import app as app_design  # This file holds our MainWindow and all design related things
# it also keeps events etc that we defined in Qt Designer
import brewer
import manager
import setup


class MakeChart(object):
    def __init__(self, title, x_label, y_label, lower_bound, upper_bound):
        values = [random.randrange(lower_bound, upper_bound) for _ in range(35)]

        def average(grades):
            return sum(grades) / len(grades)

        def generate_average(grades):
            out = []
            for period in range(1, len(grades) + 1):
                out.append(average(grades[0:period]))
            return out

        plt.ion()
        plt.plot(generate_average(values))
        plt.pause(0.001)
        plt.title(title)
        plt.ylabel(y_label)
        plt.xlabel(x_label)
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

        self.pushButton_2.clicked.connect(self.open_brewer)

    def open_brewer(self):
        Brewer().show()
        self.hide()

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

        self.label_30.setPixmap(QPixmap("assets/logo.png").scaled(320, 80))
        self.timer_count = 0

        self.pushButton.clicked.connect(self.open_manage)
        self.pushButton_2.clicked.connect(self.open_reports)

        def tick():
            self.timer_count += 1
            self.update_progress_bars(self.timer_count)
            self.update_indicators()
            # print 'tick', self.timer_count

        self.timer = QTimer()
        self.timer.timeout.connect(tick)
        self.timer.start(1000)

        self.manager = Manager()

        self.raised_a = False
        self.raised_b = False

        self.raised_1 = False
        self.raised_2 = False
        self.raised_3 = False
        self.raised_4 = False

    def open_reports(self):
        self.hide()
        self.timer.stop()
        MakeChart("Temperatures Stage 2", "Minutes from start", "Temperature", 20, 28)
        MakeChart("Level Stage 2", "Minutes from start", "Lts", 20, 1000)
        MakeChart("Pressure Stage 2", "Minutes from start", "Lts", 5,6)
        self.show()
        self.timer.start(1000)

    def open_manage(self):
        self.manager.show()

    def update_progress_bars(self, time):
        # update once every 3 seconds
        if time % 3 == 0:
            # everything is bounded to 100%
            self.process_progress.setValue(
                    self.process_progress.value() + 1 if self.process_progress.value() + 1 < 100 else 100)
            self.process_progress_2.setValue(
                    self.process_progress_2.value() + 1 if self.process_progress_2.value() + 1 < 100 else 100)
            self.process_progress_3.setValue(
                    self.process_progress_3.value() + 1 if self.process_progress_3.value() + 1 < 100 else 100)
            self.process_progress_4.setValue(
                    self.process_progress_4.value() + 1 if self.process_progress_4.value() + 1 < 100 else 100)

            if self.process_progress.value() == 100 and not self.raised_1:
                self.raise_modal(title="Notificacion",
                                 text="Un proceso de fabricacion termino",
                                 value=1,
                                 detail="El resultado del proceso 1 ya esta disponible para descargar.",
                                 message="Proceso finalizado: ")
                self.raised_1 = True

            if self.process_progress_2.value() == 100 and not self.raised_2:
                self.raise_modal(title="Notificacion",
                                 text="Un proceso de fabricacion termino",
                                 value=2,
                                 detail="El resultado del proceso 2 ya esta disponible para descargar.",
                                 message="Proceso finalizado: ")
                self.raised_2 = True

            if self.process_progress_3.value() == 100 and not self.raised_3:
                self.raise_modal(title="Notificacion",
                                 text="Un proceso de fabricacion termino",
                                 value=3,
                                 detail="El resultado del proceso 3 ya esta disponible para descargar.",
                                 message="Proceso finalizado: ")
                self.raised_3 = True

            if self.process_progress_4.value() == 100 and not self.raised_4:
                self.raise_modal(title="Notificacion",
                                 text="Un proceso de fabricacion termino",
                                 value=4,
                                 detail="El resultado del proceso 4 ya esta disponible para descargar.",
                                 message="Proceso finalizado: ")
                self.raised_4 = True

    def update_indicators(self):
        # boiler
        self.temp_lcd.display(str(float(self.temp_lcd.value()) + random.choice([-.2, .3])))
        # pressure
        self.pressure_lcd.display(str(float(self.pressure_lcd.value()) + random.choice([-.1, .1])))
        # level -> wont stop growing, will raise an alarm
        self.level_lcd.display(str(float(self.level_lcd.value()) + random.choice([.5, .8])))

        if 20 < self.level_lcd.value() < 25 and not self.raised_a:
            self.raise_modal(message="El nivel es muy alto",
                             value=self.level_lcd.value(),
                             detail="Compruebe la carga, nivel critico",
                             title="Alerta",
                             text="Un valor esta fuera de lo esperado")
            palette = self.level_lcd.palette()
            palette.setColor(self.level_lcd.backgroundRole(), QtGui.QColor('yellow'))
            self.level_lcd.paletteChange(palette)
            self.level_lcd.setAutoFillBackground(True)
            self.raised_a = True
        if 25 < self.level_lcd.value() < 28 and not self.raised_b:
            self.raise_modal(message="El nivel es anormal",
                             value=self.level_lcd.value(),
                             detail="Nivel fuera de lo comun. Compruebe el sensor",
                             title="Alerta",
                             text="Un valor esta muy fuera de rango")
            self.level_lcd.setDisabled(True)
            self.raised_b = True
        # Density
        self.density_lcd.display(str(int(self.density_lcd.value()) + random.choice([-1, 1])))

    def raise_modal(self,title,text, message, value, detail):
        #print("show message")
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setInformativeText(message + " :" + str(value))
        msg.setDetailedText(detail)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msg.show()
        msg.exec_()

    def accept(self):
        pass

    def reject(self):
        pass


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    # We set the form to be our ExampleApp (design)
    # Show the form

    app.setStyle(QtGui.QStyleFactory.create("plastique"))

    setup = SetUp()
    setup.show()

    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
