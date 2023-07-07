"""
define reverse_between() which reverses the sublist between the nodes at indices m and n 
(inclusive) in a linked list, assuming 0-based indexing. It does so by iteratively updating 
pointers within the sublist and connecting it back to the original list correctly. The use of 
a dummy node simplifies edge cases when the head of the list is part of the reversed section.


- If the linked list is empty (self.length is <= 1), return.
- Create a dummy node with value 0 and set its next pointer to the head of the linked list.
  The purpose of the dummy node is to handle cases when the head of the list is also reversed.
- Initialize a pointer prev to the dummy node.
- Iterate from 0 to m (exclusive), moving the prev pointer forward in the list. After the loop,
  prev will point to the node just before the m-th node in a 0-based index linked list. 
  In other words, prev will be at the position m-1 in the 0-based index.
- - For example, if m = 2, the loop will execute 2 times, and prev will point to the node at 
    index 1 (0-based), which is just before the node at index m.

- Set the current pointer to the node next to prev (i.e., the node at index m).

- Iterate from 0 to n - m (exclusive) to reverse the section of the linked list between 
  indices m and n. In each iteration:

- - Set temp to the node next to current (i.e., the next node to be reversed). The temp pointer
    holds the next node that will be moved to the beginning of the reversed section.

- - Update the next pointer of the current node to point to the node next to temp. This step 
    detaches temp from its current position and connects the current node to the remaining part of the sublist that is yet to be reversed.

- - Update the next pointer of the temp node to point to the node currently next to prev. 
    This step is for placing the temp node at the beginning of the reversed section.

- - Update the next pointer of the prev node to point to temp. This step connects the temp node, 
    now at the beginning of the reversed section, to the part of the list that comes before the reversed section.

- - After each iteration, the current node remains the same, but the sublist between the 
    current node and the n-th node (inclusive) is gradually reversed.

- After the loop, the section of the linked list between indices m and n is reversed. Update 
  the head of the linked list to the node next to the dummy node. This step ensures that if 
  the head of the list was reversed, the new head will be correctly assigned.
"""
from linked_list import *

def reverse_between(self, m, n):
        if self.head is None or self.head.next is None:
            return None

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        for _ in range(m):
            prev = prev.next

        current = prev.next

        for _ in range(n - m):
            temp = current.next
            current.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return self

new = LinkedList()
new.append(1)
new.append(2)   
new.append(3)
new.append(4) 
new.append(5)
new.append(6) 

print(new)

print(reverse_between(new, 0, 1))
