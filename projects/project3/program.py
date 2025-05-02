from datastructures.circularqueue import CircularQueue
from datastructures.arraystack import ArrayStack
from tests.test_arraystack import TestArrayStack, stack
from datastructures.array import Array
from projects.project3.bistro_system import bistro_system


def main():
    print('hello world')
 
    print('project 3')
   # print(q.q[1])
    b = bistro_system(['a', 'b', 'c', 'd', 'e'])
    b.run_bistro()

   


if __name__ == '__main__':
    main()
