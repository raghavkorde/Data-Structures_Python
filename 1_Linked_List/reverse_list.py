"""
Reverse a linked List : 
            tail                        head
             v          ==>              v          
head ->(1)->(2)-> None      tail ->(1)->(2)-> None   prev -> None
                                    ^
                                 current

          current                              current
             v           ==>                     v
None <-(1)->(2)-> None        None <-(1)<-(2)-> None
        ^                                  ^
       prev                               prev

Time complexity: O(n)
Space complexity: O(1)
"""
from linked_list import *

def reverse(self):
    if self.length > 1:
        current = self.head
        self.head = self.tail
        self.tail = current  
        prev = None        
        
        while current is not None:
            temp = current.next 
            current.next = prev
            prev = current
            current = temp
    return self
    


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print(linked_list)

linked_list = reverse(linked_list)
print(linked_list)
