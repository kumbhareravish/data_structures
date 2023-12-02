class DynamicArray:
    """
    Implementing dynamic array
    using static arrays in python.
    """

    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.length = 0
        self.arr = [None] * self.capacity

    # get the number of values in array.
    def get_size(self) -> int:
        return self.length
    
    # get the size of array, i.e, the number of elements it can store.
    def get_capacity(self) -> int:
        return self.capacity
    
    # returns complete array.
    def get_array(self) -> list:
        return self.arr
    
    # returns the element at index i.
    def get(self, i: int) -> int:
        if self.capacity - 1 >= i: return self.arr[i]
        else: raise IndexError("Trying to access element at index that is out of capacity of current array")
    
    # sets the element at index i to n.
    def set(self, i: int, n: int) -> None:
        if self.capacity - 1 >= i: self.arr[i] = n
        else: raise IndexError("Trying to set element at index that is out of capacity of current array")

    # sets the last element in the array to n, do not confuse the last element with index "-1",
    # here the last element means the first None vale is set to n.
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        
        self.arr[self.length] = n
        self.length += 1

    # pops and returns the last element in the array, again do not confuse l
    def popback(self) -> None:        
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr = [None] * self.capacity
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr