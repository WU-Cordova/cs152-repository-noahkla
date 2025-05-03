class drink:
    def __init__(self, name, price, ):
        self.name = name
        self.price = price
        self.qs = 0
        

    def sold(self):
        self.qs += 1