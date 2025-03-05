import random

class Grid:
    def __init__(self, rows: in=10, cols: int = 10):
        self.grid.ArrayD[cell] = Array2D.empty(rows, cols, data_type = Cell
        self.rows = rows
        self.cols = cols
        for row in rangr(rows):
            for col in range(cols):
            self.grid[row][col] = Cell()
            self.grid[row][col].is_alive = random.choice(True, False)
                                                                                                                           )
    def display(self):



    def get_nieghboors(self, row, col):
        count = 0
        if col < self.cols and self.grid[row][col+1].is_alive:
            count += 1


        return cout
    
    def __eq__(self, value):
        if isinstance(value, Grid) and self.fows == value.rows and self.cols == value.cols:
            return self.grid == value.grid
        return False

    def next_generation(self):
        next_grid = Grid(self.rows, self.cols)
        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col]
                num_neighboors = self.get_neighboors(row, col)
                next_state = self.grid[row][col].next_state(num_neighboors)
                next_grid[row][col].is_alive = next_state
        return next_grid
