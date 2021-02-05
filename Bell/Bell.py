from datetime import datetime
import os, sys, urllib.request
from PyQt5.QtWidgets import *
from time import sleep
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication

day = int(datetime.now().__str__().split(' ').__str__().split('-')[2].__str__().split("'")[0])
mounth = int(datetime.now().__str__().split(' ').__str__().split('-')[1].__str__().split("'")[0])
counter = 0
j = 0
t = 0

FORM_CLASS, _ = loadUiType("QtUi/Themes/load.ui")
ui, _ = loadUiType('QtUi/main.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        """
        try:
            open('QtUi/Themes/fileSys', 'x')
            win_day = open('QtUi/Themes/fileSys', 'w')
            win_day.write(str(day + 4))
            win_day = open('QtUi/Themes/fileSys', 'r')
        except:
            win_day = open('QtUi/Themes/fileSys', 'r')
            win = int(win_day.read())

        if day > win or mounth != 11:
            QMessageBox.about(self, 'Demo',
                              "Expired...!!!\nthank you for using this Application\nfor help Call me on the phone : +20 120 125 0706")
            win_day = open('QtUi/Themes/fileSys', 'w')

            win_day.write("000")
            quit()

        if win_day == "000":
            QMessageBox.about(self, 'Demo',
                              "Expired...!!!\nthank you for using this Application\nfor help Call me on the phone or talk to me whatsApp : +20 120 125 0706")
            quit()

        else:
        """
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUi()
        self.button()

    def InitUi(self):
        # Exit QAction
        exitQA = QAction(QIcon("QtUi\icons\exit.xpm"), "Exit", self)
        exitQA.setShortcut('Ctrl+q')
        exitQA.setStatusTip("Exit Application")
        exitQA.triggered.connect(qApp.quit)

        # About QAction
        aboutQA = QAction(QIcon("QtUi\icons\\about.xpm"), "About", self)
        aboutQA.setShortcut('Ctrl+i')
        aboutQA.setStatusTip("About")
        aboutQA.triggered.connect(self.About)

        # run Status bar --> self.statusBar()

        # run MenuBar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)

        # Add file menu
        filem = menubar.addMenu('&File')
        filem.addAction(exitQA)

        # Add help menu
        help = menubar.addMenu('&Help')
        help.addAction(aboutQA)

        self.Move_Button_setup()
        self.Move_Button_exit()
        self.Move_title()
        self.Move_lineEdit_1()
        self.Move_lineEdit_2()
        self.Move_lineEdit_3()
        self.Move_lineEdit_4()
        self.Move_lineEdit_5()
        self.Move_lineEdit_6()
        self.Move_lineEdit_7()
        self.Move_line_1()
        self.Move_line_2()
        self.Move_line_3()
        self.Move_line_4()
        self.Move_line_5()
        self.Move_line_6()
        self.Move_line_7()
        self.Move_title_v()

    def themes(self):
        os.system("cd path")
        os.system("py -3 QtUi\\themes.py")
        exit()

    def About(self):
        QMessageBox.about(self, 'About',
                          '| Welcome to the electronic bell program :\n- In this application, you can set appointments for any school, institution, or company...\n\n\t * The application was made by Kamal Ayman (oliver) *\n\nPhone - WhatsApp : +20 120 125 0706\nEmail FB (id) : kamalayman159')

    def Move_Button_setup(self):
        Setup = QPropertyAnimation(self.setup, b"geometry")
        Setup.setDuration(300)
        Setup.setStartValue(QRect(400, 477, 100, 0))
        Setup.setEndValue(QRect(400, 420, 100, 28))
        Setup.start()
        self.Setup = Setup

    def Move_Button_exit(self):
        Exit = QPropertyAnimation(self.exit, b"geometry")
        Exit.setDuration(300)
        Exit.setStartValue(QRect(40, 477, 100, 0))
        Exit.setEndValue(QRect(40, 420, 100, 28))
        Exit.start()
        self.Exit = Exit

    def Move_title(self):
        title = QPropertyAnimation(self.label_8, b"geometry")
        title.setDuration(500)
        title.setStartValue(QRect(140, 25, 460, 30))
        title.setEndValue(QRect(140, 10, 460, 30))
        title.start()
        self.title = title

    def Move_title_v(self):
        title_v = QPropertyAnimation(self.label_9, b"geometry")
        title_v.setDuration(3000)
        title_v.setStartValue(QRect(390, 34, 460, 30))
        title_v.setEndValue(QRect(390, 34, 460, 30))
        title_v.start()
        self.title_v = title_v

    def Move_lineEdit_1(self):
        L_1 = QPropertyAnimation(self.lineEdit_2, b"geometry")
        L_1.setDuration(500)
        L_1.setStartValue(QRect(300, 73, 0, 22))
        L_1.setEndValue(QRect(300, 73, 200, 22))
        L_1.start()
        self.L_1 = L_1

    def Move_lineEdit_2(self):
        L_2 = QPropertyAnimation(self.lineEdit_3, b"geometry")
        L_2.setDuration(500)
        L_2.setStartValue(QRect(500, 123, 0, 22))
        L_2.setEndValue(QRect(300, 123, 200, 22))
        L_2.start()
        self.L_2 = L_2

    def Move_lineEdit_3(self):
        L_3 = QPropertyAnimation(self.lineEdit_4, b"geometry")
        L_3.setDuration(500)
        L_3.setStartValue(QRect(300, 173, 0, 22))
        L_3.setEndValue(QRect(300, 173, 200, 22))
        L_3.start()
        self.L_3 = L_3

    def Move_lineEdit_4(self):
        L_4 = QPropertyAnimation(self.lineEdit_6, b"geometry")
        L_4.setDuration(500)
        L_4.setStartValue(QRect(500, 223, 0, 22))
        L_4.setEndValue(QRect(300, 223, 200, 22))
        L_4.start()
        self.L_4 = L_4

    def Move_lineEdit_5(self):
        L_5 = QPropertyAnimation(self.lineEdit_8, b"geometry")
        L_5.setDuration(500)
        L_5.setStartValue(QRect(300, 273, 0, 22))
        L_5.setEndValue(QRect(300, 273, 200, 22))
        L_5.start()
        self.L_5 = L_5

    def Move_lineEdit_6(self):
        L_6 = QPropertyAnimation(self.lineEdit_7, b"geometry")
        L_6.setDuration(500)
        L_6.setStartValue(QRect(500, 323, 0, 22))
        L_6.setEndValue(QRect(300, 323, 200, 22))
        L_6.start()
        self.L_6 = L_6

    def Move_lineEdit_7(self):
        L_7 = QPropertyAnimation(self.lineEdit_5, b"geometry")
        L_7.setDuration(500)
        L_7.setStartValue(QRect(300, 373, 0, 22))
        L_7.setEndValue(QRect(300, 373, 200, 22))
        L_7.start()
        self.L_7 = L_7

    def Move_line_1(self):
        l1 = QPropertyAnimation(self.label, b"geometry")
        l1.setDuration(500)
        l1.setStartValue(QRect(10, 70, 50, 31))
        l1.setEndValue(QRect(40, 70, 241, 31))
        l1.start()
        self.l1 = l1

    def Move_line_2(self):
        l2 = QPropertyAnimation(self.label_2, b"geometry")
        l2.setDuration(500)
        l2.setStartValue(QRect(10, 120, 50, 31))
        l2.setEndValue(QRect(40, 120, 241, 31))
        l2.start()
        self.l2 = l2

    def Move_line_3(self):
        l3 = QPropertyAnimation(self.label_3, b"geometry")
        l3.setDuration(500)
        l3.setStartValue(QRect(10, 170, 50, 31))
        l3.setEndValue(QRect(40, 170, 260, 31))
        l3.start()
        self.l3 = l3

    def Move_line_4(self):
        l4 = QPropertyAnimation(self.label_4, b"geometry")
        l4.setDuration(500)
        l4.setStartValue(QRect(10, 220, 50, 31))
        l4.setEndValue(QRect(40, 220, 241, 31))
        l4.start()
        self.l4 = l4

    def Move_line_5(self):
        l5 = QPropertyAnimation(self.label_6, b"geometry")
        l5.setDuration(500)
        l5.setStartValue(QRect(10, 270, 50, 31))
        l5.setEndValue(QRect(40, 270, 241, 31))
        l5.start()
        self.l5 = l5

    def Move_line_6(self):
        l6 = QPropertyAnimation(self.label_5, b"geometry")
        l6.setDuration(500)
        l6.setStartValue(QRect(10, 320, 50, 31))
        l6.setEndValue(QRect(40, 320, 241, 31))
        l6.start()
        self.l6 = l6

    def Move_line_7(self):
        l7 = QPropertyAnimation(self.label_7, b"geometry")
        l7.setDuration(500)
        l7.setStartValue(QRect(10, 370, 50, 31))
        l7.setEndValue(QRect(40, 370, 241, 31))
        l7.start()
        self.l7 = l7

    def program(self):
        day = 24 * 60 * 60 * 1000
        bell = '1'
        try:
            # Bell time
            Bell_time = self.lineEdit_2.text()
            bell_time = str(int(Bell_time) * 1000)  # Sec for arduino

            # Class_time
            Class_time = self.lineEdit_8.text()
            class_time = str(int(Class_time) * 60 * 1000 - int(bell_time))
            cc_tt = int(int(Class_time) * 60 * 1000)
            # Classes before break
            Classes_b = self.lineEdit_4.text()
            classes_b = str(int(Classes_b) + 1)

            # Classes after break
            Classes_a = self.lineEdit_6.text()
            classes_a = str(int(Classes_a) + 1)

            # Morning assembly
            Morning_a = self.lineEdit_3.text()
            morning_a = str(int(Morning_a) * 60 * 1000 - int(bell_time))

            # Break time
            Break = self.lineEdit_7.text()
            break_after_p = str(int(Break) * 60 * 1000 - int(bell_time))

            # Number days
            Number_days = self.lineEdit_5.text()
            number_days = str(int(Number_days) + 1)

            # Bell time total
            q = (int(Classes_a) * int(cc_tt))
            q2 = (int(Classes_b) * int(cc_tt))
            q3 = int(Morning_a) * 60 * 1000
            q4 = int(Break) * 60 * 1000
            qa = q + q2 + q3 + q4
            r = str(day - qa - 1000)
            Break_days = 7 - int(Number_days)
            b = str(Break_days + 1)
            arduino = """
int bell = """ + bell + """;
int x = 1;
int y = 1;
int w = 1;

void setup()
{
  pinMode(bell, OUTPUT);
}

void loop()
{
  while (1)
  {
    y = 1;
    while (y < """ + number_days + """)
    {
      digitalWrite(bell, HIGH);
      delay(""" + bell_time + """);
      digitalWrite(bell, LOW);
      delay(""" + morning_a + """);
      while (x < """ + classes_b + """)
      {
        digitalWrite(bell, HIGH);
        delay(""" + bell_time + """);
        digitalWrite(bell, LOW);
        delay(""" + class_time + """);
        x++;
      }
      digitalWrite(bell, HIGH);
      delay(""" + bell_time + """);
      digitalWrite(bell, LOW);
      delay(""" + break_after_p + """);
      x = 1;
      while (x < """ + classes_a + """)
      {
        digitalWrite(bell, HIGH);
        delay(""" + bell_time + """);
        digitalWrite(bell, LOW);
        delay(""" + class_time + """);
        x++;
      }
      digitalWrite(bell, HIGH);
      delay(""" + bell_time + """);
      digitalWrite(bell, LOW);
      delay(""" + r + """);
      x = 1;
      y++;
    }
    w = 1;
    while (w < """ + b + """) {
      delay(""" + str(day) + """);
    }
    w = 1;
    y = 1;
  }
  y = 1;
}
"""
            try:
                open("arduino.ino", "x")
                file = open("arduino.ino", "w")
                file.write(arduino)
                file.close()
                QMessageBox.information(self, "Done", "Done make Arduino file :)")
            except:
                file = open("arduino.ino", "w")
                file.write(arduino)
                file.close()
                QMessageBox.information(self, "Done", "Done make Arduino file :)")
        except:
            QMessageBox.warning(self, "Error", "make sure completed all data :(")

    def button(self):
        self.setup.clicked.connect(self.program)
        self.pushButton.clicked.connect(self.themes)
        self.exit.clicked.connect(exit)


class Splash(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(Splash, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ProgressBarValue(0)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.frame_2.setGraphicsEffect(self.shadow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(3)

    def progress(self):
        global counter
        global j
        value = counter

        html_text = """<html><head/><body><p>{value}<span style=" font-size:39pt; vertical-align:super;">%</span></p></body></html>"""
        new_text = html_text.replace("{value}", str(j))

        if value > j:
            self.label_2.setText(new_text)
            j += 10

        if value >= 100:
            value = 1.0

        self.ProgressBarValue(value)
        if counter > 100:
            self.timer.stop()
            self.window().close()

        counter += .5

    def ProgressBarValue(self, value):
        stylesheet = """QFrame{ border-radius: 150px; background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, 
        stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255)); 

}"""
        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = stylesheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.frame_2.setStyleSheet(newStylesheet)


def main():
    app = QApplication(sys.argv)
    windows = Splash()
    windows.show()
    app.exec_()
    if windows.close():
        window = MainApp()
        window.show()
        app.exec_()


if __name__ == '__main__':
    main()
