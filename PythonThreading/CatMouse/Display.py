from CatMouse.CustomString import Striscia
from threading import Lock, Thread
import time


class Display(Thread):

    def __init__(self, s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        print("First run Display")
        while not self.striscia.printStriscia():
            time.sleep(0.020)
        print("Addio topo")