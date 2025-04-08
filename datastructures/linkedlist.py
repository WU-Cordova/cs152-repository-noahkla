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
        self.head = self.tail = None
        self.count = 0

    @staticmethod
    def from_sequence(self, sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        self.head = sequence[0]
        self.tail = None

    def append(self, item: T) -> None:
        new_node = LinkedList.Node(item)
        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def prepend(self, item: T) -> None:
        new_node = LinkedList.Node(item)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
        self.count += 1


    def insert_before(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_before is not implemented")

    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

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
        count -= 1
        return data



    @property
    def front(self) -> T:
        return self.head.data

    @property
    def back(self) -> T:
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        raise NotImplementedError("LinkedList.__len__ is not implemented")

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        self.travel_node = self.travel_node.next
        return self
    
    def __reversed__(self) -> ILinkedList[T]:
        raise NotImplementedError("LinkedList.__reversed__ is not implemented")
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

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


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
