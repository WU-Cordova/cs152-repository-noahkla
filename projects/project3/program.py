from datastructures.circularqueue import CircularQueue
from datastructures.arraystack import ArrayStack
from tests.test_arraystack import TestArrayStack, stack
from datastructures.array import Array


def main():
    print('hello world')
   # a = Array([1, 2, 3])
    #print(a)
   # a.append(5)
  #  print(a)
  #  t = TestArrayStack()
    #s = stack()
   # print(t.test_push(s))
    s = ArrayStack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.peek())
    s.pop()
    print(s.pop())
   # q = CircularQueue(5)
    print("Hello, World!")
    #q.enqueue(8)
   # q.enqueue(7)
   # print(q.q[1])


   # print(q.dequeue())
    #q.front()



if __name__ == '__main__':
    main()
