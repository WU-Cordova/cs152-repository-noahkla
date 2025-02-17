# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray


from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(data_type, object):
            raise TypeError
        if not isinstance(T, Sequence):
            raise ValueError

        
        self.array = np.array(T)
        
        self.local_size = 0

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if index > np.size(self.array):
            raise IndexError
        if not isinstance(index, int) and not isinstance(index, slice):
            raise TypeError
        return self.array[T]
    
    def __setitem__(self, index: int, item: T) -> None:
        if index >np.size(self.array):
            raise IndexError
        if T.type() != self.array.dtype():
            raise TypeError
        self.array[index] = item
    

    def append(self, data: T) -> None:
        np.append(self.array, T)
    

    def append_front(self, data: T) -> None:
        np.insert(self.array, 0, T)

    def pop(self) -> None:
        raise NotImplementedError('Pop not implemented.')
    
    def pop_front(self) -> None:
        raise NotImplementedError('Pop front not implemented.')

    def __len__(self) -> int: 
        raise NotImplementedError('Length not implemented.')

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError('Equality not implemented.')
    
    def __iter__(self) -> Iterator[T]:
        raise NotImplementedError('Iteration not implemented.')

    def __reversed__(self) -> Iterator[T]:
        self.array = self.array[::-1]

    def __delitem__(self, index: int) -> None:
        np.delete(self.array, index)

    def __contains__(self, item: Any) -> bool:
        return np.isin(self.array, item)

    def clear(self) -> None:
        self.array = np.empty()
        self.local_size = 0

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__item_count}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
