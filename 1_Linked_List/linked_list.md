# Linked List

## Definition of Linked List

A linked list is a data structure that consists of a sequence of nodes, where each node contains a value and a reference (or pointer) to the next node in the sequence. It is called a "linked" list because the nodes are linked together using these references.

In a singly linked list, each node has a single reference pointing to the next node in the sequence, while in a doubly linked list, each node has references to both the next and previous nodes. The first node in the linked list is called the head, and the last node is called the tail.

Linked lists are dynamic data structures, meaning they can grow or shrink in size during program execution. They provide efficient insertion and deletion operations at any position within the list, but have slower access times compared to arrays since accessing an element requires traversing the list from the head.

## Implementation of Node Class and Linked List Class in Python


```python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.head is None:
            raise Exception("List is empty.")
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
        else:
            current = self.head
            while current.next != self.tail:
                current = current.next
            value = self.tail.value
            current.next = None
            self.tail = current
        self.length -= 1
        return value

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.head is None:
            raise Exception("List is empty.")
        value = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.length -= 1
        return value

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range.")
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    def remove(self, value):
        if self.head is None:
            raise Exception("List is empty.")
        if self.head.value == value:
            return self.pop_first()
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        if current.next is None:
            raise ValueError("Value not found in the list.")
        node_to_remove = current.next
        current.next = current.next.next
        if node_to_remove == self.tail:
            self.tail = current
        self.length -= 1

    def lookup_by_index(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def lookup_by_value(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current is not None:
            if current.next is None:
                print(f"{current.value}")
            else:
                print(f"{current.value} -> ", end='')
            current = current.next

    def __str__(self):
        current = self.head
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        return '->'.join(elements)

```



**3) Implementation of Methods in Python** 

The following methods have been implemented in the above code: 

- `append(value)`: Adds a new node with the given value at the end of the linked list. 
- `pop()`: Removes and returns the value of the last node in the linked list. 
- `prepend(value)`: Adds a new node with the given value at the beginning of the linked list. 
- `pop_first()`: Removes and returns the value of the first node in the linked list. 
- `insert(index, value)`: Inserts a new node with the given value at the specified index in the linked list. 
- `remove(value)`: Removes the first occurrence of the node with the given value from the linked list. 
- `lookup_by_index(index)`: Returns the value of the node at the specified index in the linked list. 
- `lookup_by_value(value)`: Returns `True` if a node with the given value is found in the linked list, `False` otherwise.

## Table of Runtimes

| Operation         | Time Complexity |
|-------------------|-----------------|
| append            | O(1)            |
| pop               | O(n)            |
| prepend           | O(1)            |
| pop_first         | O(1)            |
| insert            | O(n)            |
| remove            | O(n)            |
| lookup_by_index   | O(n)            |
| lookup_by_value   | O(n)            |



