"""
1.  Implement the find_middle_node method for the LinkedList class. The find_middle_node method should return 
    the middle node in the linked list WITHOUT using the length attribute.
2.  If the linked list has an even number of nodes, return the first node of the second half of the list.
3.  Keep in mind the following requirements:
        -The method should use a two-pointer approach, where one pointer (slow) moves one node at a time 
        and the other pointer (fast) moves two nodes at a time.

        -When the fast pointer reaches the end of the list or has no next node, the slow pointer should be 
        at the middle node of the list.

        -The method should return the middle node or the first node of the second half of the list if the 
        list has an even number of nodes.

        -The method should only traverse the linked list once. In other words, you can only use one loop.
"""

from linked_list import *

def find_middle_node(self):
    if self.head is None:
        raise EmptyList("List is empty")
    current = self.head
    ptr1 = current
    ptr2 = current
    while ptr2 is not None:
        if ptr2.next is None:
            mid = ptr1
            mid.next = None
            return mid
        elif ptr2.next.next is None:
            mid = ptr1.next
            mid.next = None
            return mid
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next

odd = LinkedList()
odd.append(1)
mid_one = find_middle_node(odd)
print(f"For one element: {mid_one.value} -> {mid_one.next}")
odd.append(2)
odd.append(3)
odd.append(4)
odd.append(5)

even = LinkedList()
even.append(1)
even.append(2)
mid_two = find_middle_node(even)
print(f"For two elements: {mid_two.value} -> {mid_two.next}")
even.append(3)
even.append(4)

mid_odd = find_middle_node(odd) # Should return: 3
mid_even = find_middle_node(even) # Should return: 3

print(f"mid_odd: {mid_odd.value} -> {mid_odd.next}")
print(f"mid_even: {mid_even.value} -> {mid_even.next}")