"""
This code defines a method has_loop that checks if the linked list contains a loop/cycle.
It uses Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm.

- Two pointers, slow and fast, are initialized to the head of the linked list.

- The method enters a while loop that runs as long as fast is not None and fast.next 
is not None. This is to ensure that we do not access a None value in the loop.

- Inside the loop, slow pointer moves one step at a time (slow = slow.next), while fast 
pointer moves two steps at a time (fast = fast.next.next).

- If at any point, slow and fast pointers become equal, that means there is a cycle in the 
linked list. In this case, the method returns True.

- If the loop ends without finding a cycle (i.e., the fast pointer reaches the end of the list),
 the method returns False, indicating that the linked list does not have a loop.
"""

from linked_list import *


def has_loop(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

withLoop = LinkedList()
withLoop.append(1)
withLoop.append(2)
withLoop.append(3)
withLoop.append(2)
withLoop.append(1)
withLoop.tail.next = withLoop.head

print(f"withLoop: {has_loop(withLoop)}")

withoutLoop = LinkedList()
withLoop.append(1)
withLoop.append(2)
withLoop.append(3)
withLoop.append(4)
withLoop.append(5)
withLoop.append(6)

print(f"withoutLoop: {has_loop(withoutLoop)}")