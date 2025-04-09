from datastructures.linkedlist import LinkedList
l = LinkedList()
l.append('flower')
l.append('foobar')
l.append('49ers)')
for i in l:
    print(i)
print(l.pop())