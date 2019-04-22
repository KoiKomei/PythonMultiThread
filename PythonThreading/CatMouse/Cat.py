from CatMouse.CustomString import Striscia
from threading import Lock, Thread
import time

class Cat(Thread):

    def __init__(self, s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        print("First run cat")
        while not self.striscia.moveCat():
            time.sleep(0.100)