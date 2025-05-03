from datastructures.circularqueue import CircularQueue
from datastructures.arraystack import ArrayStack
from tests.test_arraystack import TestArrayStack, stack
from datastructures.array import Array
from projects.project3.bistro_system import bistro_system
from projects.project3.drink import drink
from datastructures.hashmap import HashMap


def main():
    m = HashMap()
    m['Drip Coffee'] = drink('Drip Coffee', 2.50)
    m['Calpico Lemonade'] = drink('Calpico Lemonade', 3 )
    m['Bannana Milk'] = drink('Bannana Milk', 2)
    m['Golden Milk Latte'] = drink('Golden Milk Latte', 4)
    m['Coconut Milk Tea Latte'] = drink('Coconut Milk Tea Latte', 6)
    print('project 3')
   # print(q.q[1])
    b = bistro_system(m)
    b.run_bistro()

   


if __name__ == '__main__':
    main()
