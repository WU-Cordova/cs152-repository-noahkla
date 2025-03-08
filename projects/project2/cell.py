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
        
        