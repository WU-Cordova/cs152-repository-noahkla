import random
import numpy as np
#from projects.project2.cell import Cell
#from datastructures.array2d import Array2D
class Cell:
    def __init__(self, is_alive):
        self.is_alive = is_alive

    def next_state(self, num_neighboors):
        if num_neighboors == 0 or num_neighboors ==1 or num_neighboors >= 4:
            a = False
        if num_neighboors == 3:
            a = True
        if num_neighboors == 2:
            a = self.is_alive
     #   print(a)
        return a
    def show_cell(self):
        if self.is_alive == True:
            print('🦠', end = '')
        else:
            print('X', end = ' ')
        
        
        
class Grid:
    def __init__(self, rows: int=10, cols: int = 10):
      #  self.grid.ArrayD[Cell] = Array2D.empty(rows, cols, data_type = Cell)
        self.grid = np.array([[None]*rows]*cols)
        self.rows = rows
        self.cols = cols
        for i in range(rows):
            for j in range(cols):
           # self.grid[row][col] = Cell()
                self.grid[i][j] = Cell(random.choice([True, False]))
            #    print(i, j)
       # self.display()                                                                                                                           
    def display(self):
        for i in range(self.rows):
            
            for j in range(self.cols):
                self.grid[i][j].show_cell()
            print('\n')
        


    def get_neighboors(self, row, col):
        count = 0
        
        for i in range(3):
            for j in range(3):
                try:
                    if not ((i==1 and j==1) or row+i-1<0 or col+j-1<0):
                        count += self.grid[row+i-1][col+j-1].is_alive
                      #  print(i-1, j-1)
                       # print(self.grid[row+i-1][col+j-1].is_alive)
                except:
                    pass
            
       


        return count
    
    def __eq__(self, value):
        if isinstance(value, Grid) and self.rows == value.rows and self.cols == value.cols:
            for r in range(self.rows):
                if self.grid[r] != value.grid[r]:
                    return False
        return True

    def next_generation(self):
        next_grid = Grid()
       # next_grid.display()
        for row in range(self.rows):
            for col in range(self.cols):
              #  self.grid[row][col]
                num_neighboors = self.get_neighboors(row, col)
                next_state = self.grid[row][col].next_state(num_neighboors)
                next_grid.grid[row][col].is_alive = next_state
    #    next_grid.display()
        return next_grid
from time import sleep
from kbhit import KBHit

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
            self.grid = self.grid.next_generation()
            #if self.grid == self.history:
            if g >25:
                return
            sleep(1)
            #if kbhit:
             #   pass
#g = Grid()
#g.display()
#print(g.get_neighboors(9, 9))
#g = g.next_generation()
#g.display()
#g = g.next_generation()
#g = g.next_generation()
g = GameController()
g.run()
