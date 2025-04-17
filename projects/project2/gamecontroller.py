#from datastructures.array2d import Array2D
from projects.project2.kbhit import KBHit
from projects.project2.grid import Grid
from time import sleep
#from projects.project2.kbhit import KBHit

class GameController:
    def __init__(self):
        self.grid = Grid()
        self.history = []
        self.previous = Grid()
    def run(self):
        print(' A for Automatic mode or M for manual')
        m = input()
        if m == 'A':
            m = False
        if m == 'M':
            m = True
        else:
            m = False
       # kbhit = KBHit.kbhit()
        g = 1
        while True:

            print('Generation '+ str(g) + ':')
            g += 1
            self.grid.display()
            if self.grid == self.previous:
                print('It is stable!')
                return
            if self.grid in self.history:
                print('It is unstable')
                return
            self.history.append(self.grid)
            self.previous = self.grid
            if len(self.history)>6:
                del self.history[0]
           # print('yeet')
            self.grid = self.grid.next_generation()
            #if self.grid == self.history:
            
           # c = True
            #for i in range(self.grid.rows):
                #for j in range(self.grid.cols):
                    #if self.grid.grid[i][j] != self.history.grid[i][j]:
                        #c = False
                        #if g>100:
                            
          #  if c:
             #   print('They are equal!!!')
              #  return

           # if g>150:
             #   print('24!!!')
              #  return

            if m:
                print('q to quit, c to go to next generation, a to go to automatic mode')
                x = input()
                if x == 'q':
                    return
                if x == 'a':
                    m = False
            kb = KBHit()
            if kb.kbhit():
                k = kb.getch()
                if k == 'm' or 'M':
                    m = True
            
            if not m:
                pass
                sleep(1)
    
    