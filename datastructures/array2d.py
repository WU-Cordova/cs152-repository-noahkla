from __future__ import annotations
import os
from typing import Iterator, Sequence
#from numpy import np
from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: Array, num_columns: int):
            self.elements2d = Array()
            self.num_columns = num_columns
            self.row_index = row_index 
        
            


        def __getitem__(self, column_index: int) -> T:
            return self.elements2d[column_index]
        
        def __setitem__(self, column_index: int, value: T) -> None:
            self.elements2d[column_index] = value
        
        def __iter__(self) -> Iterator[T]:
            return iter[self.elements2d]
        
        def __reversed__(self) -> Iterator[T]:
            return iter(self.elemenst2d[::-1])

        def __len__(self) -> int:
            return len(self.rows_len)
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        if not isinstance(starting_sequence, Sequence):
            raise ValueError
        self.data_type = data_type
        self.rows_len = len(starting_sequence)
        self.cols_len = len(starting_sequence[0])

        print('starting')
        self.array = []

        for row in range(self.rows_len):
            
          #  for col in range(self.cols_len):
           #         py_list.append(starting_sequence[row][col])

            if len(starting_sequence[row]) != self.rows_len:
                raise ValueError
            self.array.append(self.Row(starting_sequence[row]))
            for i in starting_sequence[row]:
                if i.type != data_type:
                    raise ValueError

      #  self.array = Array()
       # for i in range(len(starting_sequence)):
        #    self.array.append(self.Row(self, i, len(starting_sequence[0])))
         #       self.array[i].__setitem__(starting_sequence[i])

    @staticmethod
    def empty(self, rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        self.array = Array2D()

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        return self.array[row_index]
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        return iter(self.array)
    
    def __reversed__(self):
        return iter(self.array[::-1])
    
    def __len__(self): 
        return self.rows_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'Array2D {self.__num_rows} Rows x {self.__num_columns} Columns, items: {str(self)}'


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')