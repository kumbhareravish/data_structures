# A node class that defines a basic unit of linked list
class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

class LinkedList:
    """
    Implementing singly linked list in python (in progress)
    """
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def get(self) -> list:
        arr = []
        temp_node = self.head
        while temp_node:
            arr.append(temp_node.data)
            temp_node = temp_node.next
        return arr
    
    def length(self) -> int:
        len = 0
        temp_node = self.head
        while temp_node:
            len += 1
            temp_node = temp_node.next
        return len

    def insertAtBegin(self, value) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, index, value) -> None:
        new_node = Node(value)
        if index == 0:
            self.insertAtBegin(value)
        elif index > self.length():
            raise IndexError("Given index is out of range for current linked list.")
        else: 
            temp_node = self.head
            for i in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    def insertAtEnd(self, value):
        new_node = Node(value)
        temp_node = self.head
        while temp_node.next:
            temp_node = temp_node.next
        temp_node.next = new_node

    def update(self, index, value) -> None:
        temp_node = self.head
        for i in range(index):
            temp_node = temp_node.next
        if temp_node:
            temp_node.data = value
        else:
            raise IndexError("Given index is out of range for current linked list.")

    def deleteFirst(self) -> None:
        if self.head:
            self.head = self.head.next
        else: # For empty linked list
            raise ValueError("Cannot remove from an empty linked list.")

    def deleteLast(self) -> None:
        if not self.head: # For empty linked list
            raise ValueError("Cannot remove elements from empty linked list.")
        elif self.head.next: # If linked list contains only 1 element, then above current_node.next.next raises error
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None
        else: # If linked list contains more than 1 element
            self.head = None

    def deleteAtindex(self, index) -> None:
        pass

    def deleteByValue(self, value) -> None:
        pass
