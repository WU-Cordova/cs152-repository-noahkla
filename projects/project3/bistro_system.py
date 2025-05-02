from drink import drink
from custom_order import custom_order
from datastructures.arraystack import ArrayStack
from datastructures.linkedlist import LinkedList
class bistro_system:
    def __init__(self, menu: list[drink]):
        self.menu = menu
        self.r = 0
        self.orders = LinkedList(data_type = custom_order)
    def add_order(self, index, quantity):
        for i in range(quantity):
            self.orders.prepend(self.menu[index])
    def complete_order(self):
        self.r += self.orders.pop_front().p
    def print_menu(self):
        print('Bearcat Bistro Menu:')
        for i in range(len(self.menu)):
            print(str(i)+'. '+self.menu[i].name + ' - '+ '$' + self.menu[i].price)
    def end_of_day(self):
        print('Drink Name \t Qty Sold \t Total Sales')
        for item in self.menu:
            print(item.name+'\t'+str(item.qs)+'\t'+str(item.qs*item.price))
        print('Total Revenue: \t \t'+ str(self.r))
    
    def run_bistro(self):
        print('Welcome to the Bearcat Bistro!')
        print('1. Display Menu')
        print('2. Take New Order')
        print('3. View Open Orders')
        print('4. Mark Next Order as complete')
        print('5. View end of day report')
        print('6. Exit')


        

    