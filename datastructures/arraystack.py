import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       

        '''
        self.max_size = max_size
        self.a = []
        #elf.a = Array]*)
    def push(self, item: T) -> None:
        self.a.append(item)

    def pop(self):
       return self.a.pop()

    def clear(self) -> None:
       self.a = []
    @property
    def peek(self) -> T:
       return self.a[len(self.a)-1]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.max_size    
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        if len(self.a) >= self.max_size:
            return True
        return False

    @property
    def empty(self) -> bool:
        raise NotImplementedError
    def __eq__(self, other: object) -> bool:
       return self.a == other.a

    def __len__(self) -> int:
       return len(self.a)
    
    def __contains__(self, item: T) -> bool:
       return item in self.a

    def __str__(self) -> str:
        return str([self.stack[i] for i in range(self._top)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

