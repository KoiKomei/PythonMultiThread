import random
from threading import Lock


class Striscia:
    SIZE = 20

    def __init__(self):
        self.striscia = list()
        self.end = False
        self.dirCat = 1
        self.mouse = random.randint(0, self.SIZE-1)
        self.cat = random.randint(0, self.SIZE-1)
        self.lock = Lock()
        for i in range(0, self.SIZE):
            self.striscia.append(' ')
        self.striscia[self.mouse] = '.'
        self.striscia[self.cat] = '*'

    def printStriscia(self):
        self.lock.acquire()
        try:
            print("|%s|" % ''.join(self.striscia))
            return self.end
        finally:
            self.lock.release()

    def moveCat(self):
        self.lock.acquire()
        try:
            if self.end:
                return True
            self.striscia[self.cat]= ' '

            self.cat += self.dirCat
            if self.cat > self.SIZE-1 or self.cat < 0:
                self.dirCat = -self.dirCat
                self.cat += 2* self.dirCat

            if self.cat == self.mouse:
                self.end = True
                self.striscia[self.cat] = '@'
                return True

            self.striscia[self.cat] = '*'
            return False
        finally:
            self.lock.release()

    def moveMouse(self):
        self.lock.acquire()
        try:
            if self.end:
                return True

            self.striscia[self.mouse] = ' '

            self.jump = random.randint(-1,1)
            if self.mouse + self.jump >= 0 and self.mouse + self.jump < self.SIZE:
                self.mouse = self.mouse + self.jump

            if self.cat == self.mouse:
                self.end = True
                self.striscia[self.mouse] = '@'
                return True

            self.striscia[self.mouse] = '.'

            return False
        finally:
            self.lock.release()
