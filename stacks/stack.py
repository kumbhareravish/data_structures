class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack():
    """
    implementation of stack using singly linked list (in progress)
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def get(self) -> list:
        arr = []
        temp_node = self.head
        while temp_node:
            arr.insert(0, temp_node.data)
            temp_node = temp_node.next
        return arr

    def push(self, value) -> None:
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def pop(self) -> int:
        if self.is_empty():
            raise ValueError("Stack is empty.")
        element = self.head.data
        self.head = self.head.next
        self.length -= 1
        return element

    def peek(self):
        if self.is_empty():
            raise ValueError("Stack is empty.")
        return self.head.data

    def is_empty(self):
        return not self.head