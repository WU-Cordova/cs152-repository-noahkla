from datastructures.linkedlist import LinkedList
from drink import drink
class custom_order:
    def __init__(self):
        self.order = LinkedList(data_type=drink)
        self.p = 0
    def add_item(self, item: drink):
        self.order.append(item)
        self.p += item.price
    def item_completed(self, item: drink):
        self.order.remove(item)
    def print_order(self):
        for item in self.order:
            print('item: '+ item.name)
            print('cost: '+ item.price)
        print('total cost: '+ self.p)

        