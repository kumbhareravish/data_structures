# A node class that defines a basic unit of linked list
class Node:
    def __init__(self, value) -> None:
        self.value = value
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
        while temp_node is not None:
            arr.append(temp_node.value)
            temp_node = temp_node.next
        return arr
    
    def length(self) -> int:
        len = 0
        temp_node = self.head
        while temp_node is not None:
            len += 1
            temp_node = temp_node.next
        return len

    def insertAtBegin(self, value) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtPos(self, pos, value) -> None:
        new_node = Node(value)
        if pos == 0:
            self.insertAtBegin(value)
        elif pos > self.length():
            raise IndexError("Given position out of range for current linked list.")
        else: 
            temp_node = self.head
            for i in range(pos-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

    def insertAtEnd(self, value):
        new_node = Node(value)
        temp_node = self.head
        while temp_node.next is not None:
            temp_node = temp_node.next
        temp_node.next = new_node

    def update(self, value) -> None:
        pass

    def deleteFirst(self) -> None:
        pass

    def deleteLast(self) -> None:
        pass

    def deleteAtPos(self, pos) -> None:
        pass

    def deleteByValue(self, value) -> None:
        pass
