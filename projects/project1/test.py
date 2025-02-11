class data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if (self.x, self.y) == other:
            return True
        return False

    def __hash__(self):
        return hash((self.x, self.y))
        
