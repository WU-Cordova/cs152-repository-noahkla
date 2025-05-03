from projects.project3.drink import drink
from projects.project3.custom_order import custom_order
from datastructures.arraystack import ArrayStack
from datastructures.linkedlist import LinkedList
from datastructures.hashmap import HashMap
class bistro_system:
    def __init__(self, menu: HashMap):
        self.menu = menu
        self.r = 0
        self.orders = LinkedList(data_type = custom_order)
        self.completed_orders = LinkedList(data_type = custom_order)
   # def add_order(self, index, quantity):
    #    for i in range(quantity):
     #       self.orders.prepend(self.menu[index])

    def complete_order(self):
        x = self.orders.pop_front()
        self.r += x.p
        self.completed_orders.append(x)
        self.menu[x.order[0].name].qs += 1
        

    def print_menu(self):
        print('Bearcat Bistro Menu:')
        j = 1
        for i in self.menu:
            print(str(j)+'. '+self.menu[i].name + ' - '+ '$' + str(self.menu[i].price))
            j += 1

    def end_of_day(self):
      #  print('Drink Name \t Qty Sold \t Total Sales')
        for item in self.menu:
            item = self.menu[item]
            print(item.name+'\t''Quanitity sold: '+str(item.qs)+'\t''Total Sales: $'+str(item.qs*item.price))
        print('Total Revenue: $'+ str(self.r))
    
    def print_orders(self):
        for o in self.orders:
            o.print_order()
    
    def run_bistro(self):
        while True:
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
            if x == '2':
                print('Enter what you want:')
                y = input()
                if y not in self.menu:
                    print('This is not in the menu. Try Again!')
                    continue
                print('What size do you want it?')
                s = input()
                print ('Any custom instructions?')
                z = input()
                print('what is your name?')
                p = input()
                c = custom_order(p)
                c.add_item(self.menu[y], size = s, customization=z)
                self.orders.append(c)
            if x == '3':
                self.print_orders()
            if x == '4':
                self.complete_order()
            if x == '5':
                self.end_of_day()
            if x == '6':
                return
            print('\n')




        

    