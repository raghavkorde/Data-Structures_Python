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

    def reverse(self):
        if self.length > 1:
            current = self.head
            prev = None
            while current is not None:
                # next_node stores the reference to the next node before we modify the current.next reference.
                next_node = current.next # next_node is pointer to the next node from current
                
                # Reverses the link between the current node and its next node.
                current.next = prev # set pointer to the next node to pointer to the previous node (previous iteration)
                
                # This ensures that we have the correct reference to the previous node for the next iteration of the loop.
                prev = current # set prev to the current node
                
                # Moves our position in the linked list forward to the next node, preparing for the next iteration of the loop.
                current = next_node # set current to the next node pointer
            
            self.head = prev

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

def main():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print(linked_list)

    linked_list.pop()
    print(linked_list)

    linked_list.pop_first()
    print(linked_list)

    linked_list.append(3)
    linked_list.prepend(1)
    print(linked_list)

    linked_list.insert(2, 2.5)
    linked_list.insert(1, 1.5)
    print(linked_list)

    linked_list.remove(2.5)
    linked_list.remove(1.5)
    print(linked_list)

    
    print(linked_list.lookup_by_index(1))
    
   
    # print(linked_list.lookup_by_index(5)) #will raise IndexError("Index out of range.")

    print(linked_list.lookup_by_value(3))
    print(linked_list.lookup_by_value(0))



if __name__ == "__main__":
    main()
