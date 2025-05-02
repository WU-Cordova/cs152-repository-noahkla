from datastructures.linkedlist import LinkedList
from projects.project3.drink import drink
class custom_order:
    def __init__(self, name):
        self.order = LinkedList(data_type=drink)
        self.p = 0
        self.name = name
    def add_item(self, item: drink, size, customization):
        self.order.append(item)
        self.p += item.price
        self.s = size
        self.c = customization
    def item_completed(self, item: drink):
        self.order.remove(item)
    def print_order(self):
        for item in self.order:
            print('item: '+ item.name)
            print('cost: '+ str(item.price))
            print('size: ' + str(self.s))
            print('customization: '+self.c)
            print('name: '+ self.name)
    
       # print('total cost: '+ self.p)

        