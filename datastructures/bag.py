from typing import Iterable, Optional
from datastructures.ibag import IBag, T

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.b = {}
        for item in items:
            self.add(item)

    def add(self, item: T) -> None:
        if item in self.b:
            self.b[item] += 1
        elif item != None:
            self.b[item] = 1
        else:
            raise TypeError

    def remove(self, item: T) -> None:
        if item in self.b:
            if self.b[item] >1:
                self.b[item] -= 1
            else:
                del self.b[item]
        else:
            raise ValueError
        

    def count(self, item: T) -> int:
        if item in self.b:
            return self.b[item]
        return 0

    def __len__(self) -> int:
        c = 0
        for item in self.b:
            c += self.b[item]
        return c

    def distinct_items(self) -> int:
        return self.b.keys()

    def __contains__(self, item) -> bool:
        return item in self.b

    def clear(self) -> None:
        self.b = {}
