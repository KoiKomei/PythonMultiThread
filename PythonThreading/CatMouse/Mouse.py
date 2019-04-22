from CatMouse.CustomString import Striscia
from threading import Lock, Thread
import time

class Mouse(Thread):

    def __init__(self, s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        print("First run mouse")
        while not self.striscia.moveMouse():
            time.sleep(0.050)