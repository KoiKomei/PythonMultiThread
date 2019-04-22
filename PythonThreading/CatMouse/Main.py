from CatMouse.CustomString import Striscia
from CatMouse.Mouse import Mouse
from CatMouse.Cat import Cat
from CatMouse.Display import Display

print("Start of the game")

striscia = Striscia()
jerry = Mouse(striscia)
tom = Cat(striscia)
display = Display(striscia)
print("Done")

display.start()
jerry.start()
tom.start()
print("Started")