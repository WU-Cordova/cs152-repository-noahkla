#from datastructures.array2d import Array2D
#from kbhit import KBHit
from projects.project2.grid import Grid
from time import sleep
from time import sleep
#from projects.project2.kbhit import KBHit

class GameController:
    def __init__(self):
        self.grid = Grid()
        self.history = Grid()
    def run(self):
       # kbhit = KBHit.kbhit()
        g = 1
        while True:
            print('Generation '+ str(g))
            g += 1
            self.grid.display()
            self.history = self.grid
            print('yeet')
            self.grid = self.grid.next_generation()
            #if self.grid == self.history:
            if g >25:
                return
            sleep(1)
            print('foobar')
    
    