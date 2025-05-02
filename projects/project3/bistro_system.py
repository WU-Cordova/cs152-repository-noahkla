from projects.project3.drink import drink
from projects.project3.custom_order import custom_order
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
            print(str(i)+'. '+self.menu[i].name + ' - '+ '$' + str(self.menu[i].price))
    def end_of_day(self):
        print('Drink Name \t Qty Sold \t Total Sales')
        for item in self.menu:
            print(item.name+'\t'+str(item.qs)+'\t'+str(item.qs*item.price))
        print('Total Revenue: \t \t'+ str(self.r))
    
    def print_orders(self):
        for o in self.orders:
            o.print_order()
    
    def run_bistro(self):
        print('Welcome to the Bearcat Bistro!')
        print('1. Display Menu')
        print('2. Take New Order')
        print('3. View Open Orders')
        print('4. Mark Next Order as complete')
        print('5. View end of day report')
        print('6. Exit')
        x = input()
        if x == '1':
            self.print_menu()
            self.run_bistro()
        if x == 2:
            print('enter the index of the order from the menu:')
            y = input()
            y = int(y)
            self.add_order(y)
            self.run_bistro()
        if x == 3:
            self.print_orders()
        if x == 4:
            self.complete_order()
        if x == 5:
            self.end_of_day()
        if x == 6:
            return




        

    