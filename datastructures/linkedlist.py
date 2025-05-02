from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count = 0

    @staticmethod
    def from_sequence(self, sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        self.head = sequence[0]
        self.tail = None

    def append(self, item: T) -> None:
        new_node = LinkedList.Node(item)
        if self.count == 0:
            self.tail = self.head = new_node
            self.count += 1
            return
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def prepend(self, item: T) -> None:
        new_node = LinkedList.Node(item)
        if self.count == 0:
            self.tail = self.head = new_node
            self.count += 1
            return
        
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        self.count += 1


    def insert_before(self, target: T, item: T) -> None:
        new_node = LinkedList.Node(item)
        n = self.head
        while n:
            if n.data == item:
                n.previous.next = new_node
                new_node.next = n
                new_node.previous = n.previous
                n.previous = new_node
                self.count += 1
                return
            n = n.next

    def insert_after(self, target: T, item: T) -> None:
        new_node = LinkedList.Node(item)
        n = self.head
        while n:
            if n.data == item:
                n.next.previous = new_node
                new_node.next = n.next
                new_node.previous = n
                n.next = new_node
                self.count += 1
                return
            n = n.next

    def remove(self, item: T) -> None:
        n = self.head
        while n:
            if n.data == item:
                n.previous.next = n.next
                n.next.previous = n.previous
                self.count -= 1
                return
            n = n.next

    def remove_all(self, item: T) -> None:
        n = self.head
        while n:
            if n.data == item:
                n.previous.next = n.next
                n.next.previous = n.previous
                self.count -= 1
            n = n.next

    def pop(self) -> T:
        if self.count == 0:
            raise IndexError
        if self.count == 1:
            data = self.head.data
            self.head = self.tail = None
            
        else:
            data = self.tail.data
            self.tail.previous.next = None
            self.tail = self.tail.previous
        self.count -= 1
        return data


    def pop_front(self) -> T:
        if self.count == 0:
            raise IndexError
        data = self.head.data
        if self.count == 1:
            data = self.head.data
            self.head = self.tail = None
        else:
            self.head.next.previous = None
            self.head = self.head.next
        self.count -= 1
        return data



    @property
    def front(self) -> T:
        if self.count == 0:
            raise IndexError
        return self.head.data

    @property
    def back(self) -> T:
        if self.count == 0:
            raise IndexError
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.tail = self.head = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        n = self.head
        while n:
            if n.data == item:
                return True
            n = n.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration
        data = self.travel_node.data
        self.travel_node = self.travel_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        l = []
        n = self.tail
        while n:
            l.append(n)
            n = n.previous
        return iter(l)

    
    def __eq__(self, other: object) -> bool:
        l = []
        n = self.head
        while n:
            l.append(n.data)
            n = n.next
        o = []
        o2 = other.head
        while o2:
            o.append(o2.data)
            o2 = o2.next
        print(l, o)
        return l == o

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"
    
    def __getitem__(self, k):
        if k > self.count-1 or k<0:
            raise IndexError
        n = self.head
        for i in range(k):
            n = n.next
        return n.data
    def __setitem__(self, k, v):
        if k > self.count-1 or k<0:
            raise IndexError
        n = self.head
        for i in range(k):
            n = n.next
        n.data = v
    def __delitem__(self, k):
        if k > self.count-1 or k<0:
            raise IndexError
        n = self.head
        for i in range(k):
            n = n.next
        n.previous.next = n.next
        n.next.previous = n.previous
        self.count -= 1


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
