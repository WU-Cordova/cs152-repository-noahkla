import random
import numpy as np
from projects.project2.cell import Cell
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
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j].is_alive != value.grid[i][j].is_alive:
                    return False
       
        return True

    def next_generation(self):
        next_grid = Grid()
       # next_grid.display()
        for row in range(self.rows):
            for col in range(self.cols):
              #  self.grid[row][col]
                num_neighboors = self.get_neighboors(row, col)
                if num_neighboors == None:
                    print('Issue!!!')
                next_state = self.grid[row][col].next_state(num_neighboors)
                next_grid.grid[row][col].is_alive = next_state
    #    next_grid.display()
        return next_grid


        return count