from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.b = {}
        for item in items:
            self.add(item)

    def add(self, item: T) -> None:
        if T in self.b:
            self.b[T] += 1
        else:
            self.b[T] = 1

    def remove(self, item: T) -> None:
        if T in self.b:
            if self.b[T] >1:
                self.b[T] -= 1
            else:
                del self.b[T]

    def count(self, item: T) -> int:
        return self.b[T]

    def __len__(self) -> int:
        c = 0
        for item in self.b:
            c += self.b[item]
        return c

    def distinct_items(self) -> int:
        items = []
        for item in self.b:
            items.append(item)
        return items

    def __contains__(self, item) -> bool:
        return item in self.b

    def clear(self) -> None:
        self.b = {}
