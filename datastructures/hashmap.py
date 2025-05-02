import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib
from math import sqrt
from datastructures.linkedlist import LinkedList
import numpy as np

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets = np.empty(shape = 7, dtype = LinkedList)
        for i in range(len(self._buckets)):
            self._buckets[i] = LinkedList()
        
        self.n = number_of_buckets
        self.count = 0
        self._load_factor = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function
    def __getitem__(self, key: KT) -> VT:
        hv = self._hash_function(KT)%self.n
        for (k, v) in self._buckets[hv]:
            if k == key:
                return v
        raise KeyError

    def __setitem__(self, key: KT, value: VT) -> None:        
        hv = self._hash_function(KT)%self.n
        for i in range(len(self._buckets[hv])):
            if self._buckets[hv][i][0] == key:
                self._buckets[hv][i] = (key, value)
                return
        self._buckets[hv].append((key, value))
        self.count += 1
       # if self.count > self._load_factor*self.n:
           # self.resize(self.next_prime_after_double(self.n))


    def keys(self) -> Iterator[KT]:
        raise
    
    def values(self) -> Iterator[VT]:
        raise NotImplementedError("HashMap.values() is not implemented yet.")

    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError("HashMap.items() is not implemented yet.")
            
    def __delitem__(self, key: KT) -> None:
        if key>self.count-1:
            raise KeyError
        hv = self._hash_function(KT)%self.n
        for i in range(len(self._buckets[hv])):
            print(i, len(self._buckets[hv]))
            if self._buckets[hv][i][0] == key:
                del self._buckets[hv][i]
                self.count -= 1
        
    
    def __contains__(self, key: KT) -> bool:
        bucket_index = self._hash_function(KT)%self.n
        bucket_chain = self._buckets[bucket_index]
        for (k, v) in bucket_chain:
            if k == key:
                return True
        return False
    
    def __len__(self) -> int:
        return self.count
    
    def __iter__(self) -> Iterator[KT]:
        keys = []
        for b in self._buckets:
            for h in b:
                keys.append(h[0])
        keys.sort()
        return iter(keys)
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("HashMap.__eq__() is not implemented yet.")

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"
    def next_prime_after_double(self, n):
        n = 2*n+1
        while True:
            c = True
            for i in range(2, int(sqrt(n))+1):
                if n%i ==0:
                    c = False
            if c:
                return n
            n += 1
    def resize(self, s):
        h = HashMap(number_of_buckets=s)
        for b in self._buckets:
            for (k, v) in b:
                h[k] = v
        self._buckets = h._buckets
        self.count = h.count
        self.n = h.n

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.

        """
        
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)