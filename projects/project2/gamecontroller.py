from datastructures.array2d import Array2D
from msvcrt import kbhit
from projects.project2.grid import Grid
from time import sleep
class GameController:
    def __init__(self):
        self.grid = Grid()
        self.history = Grid()
    def run(self):
        kbhit = kbhit()
        while True:
            self.grid.display()
            sleep(1)
            if kbhit:
                pass
    
    