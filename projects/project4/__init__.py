from datastructures.linkedlist import LinkedList
from datastructures.deque import Deque
l = LinkedList()
l.append('flower')
l.append('foobar')
l.append('49ers)')
for i in l:
    print(i)
print(l.pop())
d = Deque()
d.enqueue(10)
d.enqueue(20)
print(d.dequeue())
print("Hello, World!")