"""
Insert a node at a given index using recursion
Space: O(n); Time:O(n)
"""
from linked_list import *

def insertRecursion(head, value, index):
    if index == 0:
        new_node = Node(value)
        new_node.next = head
        return new_node

    if index < 0 or not head:
        raise IndexError("Index out of range")

    head.next = insertRecursion(head.next, value, index - 1)
    return head

new_list = LinkedList()
new_list.append(3)
new_list.append(5)
new_list.append(9)
new_list.append(1)

current = LinkedList()
current.head = insertRecursion(new_list.head, 7, 2)
print(current)


