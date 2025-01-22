from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.b = {}
        raise NotImplementedError("__init__ method not implemented")

    def add(self, item: T) -> None:
        if T in self.b:
            self.b[T] += 1
        else:
            self.b[T] = 1
        raise NotImplementedError("add method not implemented")

    def remove(self, item: T) -> None:
        if T in self.b:
            if self.b[T] >1:
                self.b[T] -= 1
            else:
                del self.b[T]
        raise NotImplementedError("remove method not implemented")

    def count(self, item: T) -> int:
        return self.b[T]
        raise NotImplementedError("count method not implemented")

    def __len__(self) -> int:
        c = 0
        for item in self.b:
            c += self.b[item]
        return c
        raise NotImplementedError("__len__ method not implemented")

    def distinct_items(self) -> int:
        items = []
        for item in self.b:
            items.append(item)
        return items
        raise NotImplementedError("distinct_items method not implemented")

    def __contains__(self, item) -> bool:
        return item in self.b
        raise NotImplementedError("__contains__ method not implemented")

    def clear(self) -> None:
        self.b = {}
        raise NotImplementedError("clear method not implemented")