"""
This code defines a function find_kth_from_end(self, k) that finds the k-th node from the end 
of a linked list. The function takes two arguments, ll representing the linked list and k 
representing the position of the node to be found from the end.

- The function initializes two pointers, slow and fast, both initially pointing to the head of 
  the linked list.

- It then moves the fast pointer k nodes ahead in the list. If fast becomes None before moving 
  k steps, it means the list is shorter than k nodes, and the function returns None.

- Once the fast pointer is k nodes ahead, the function enters a loop that continues until the 
  fast pointer reaches the end of the list.

- Inside the loop, both the slow and fast pointers move one node forward at each iteration.

- When the fast pointer reaches the end of the list, the slow pointer will be at the k-th node
  from the end of the list.

- The function returns the slow pointer, which points to the k-th node from the end.

>This algorithm is known as the "tortoise and hare" or "two-pointer" technique and allows us to
find the k-th node from the end of a singly linked list in a single pass with O(n) time 
complexity.
"""

from linked_list import *

def find_kth_from_end(self, k):
    slow = self.head
    fast = self.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow

ll = LinkedList()
ll.append(2)
ll.append(4)
ll.append(6)
ll.append(8)
ll.append(10)
ll.append(12)

print(f"3rd Last: {find_kth_from_end(ll, 3).value}")
print(f"Last: {find_kth_from_end(ll, 1).value}")
print(f"First: {find_kth_from_end(ll, 6).value}")