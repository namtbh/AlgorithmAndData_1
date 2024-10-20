import time
import random

# Node class represents a single element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data (an integer)
        self.next = None  # Pointer to the next node in the list

# LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list (no head node)
    
    # Add a new node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # New node points to the old head
        self.head = new_node  # Now, the new node becomes the head
    
    # Add a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:  # If the list is empty, make the new node the head
            self.head = new_node
            return
        last = self.head
        while last.next:  # Traverse the list to find the last node
            last = last.next
        last.next = new_node  # The last node now points to the new node
    
    # Delete nodes from the beginning, one by one
    def delete_from_beginning(self):
        while self.head:  # Keep deleting until the list is empty
            temp = self.head
            self.head = self.head.next  # Move the head to the next node
            del temp
    
    # Delete nodes from the end, one by one
    def delete_from_end(self):
        while self.head:  # Keep deleting until the list is empty
            if not self.head.next:  # If there's only one node, delete it
                del self.head
                self.head = None
                return
            second_last = self.head
            while second_last.next.next:  # Traverse to the second-to-last node
                second_last = second_last.next
            del second_last.next  # Delete the last node
            second_last.next = None  # Set the new last node's next to None

# Function to test the performance of inserting and deleting nodes
def performance_test():
    linkedList1 = LinkedList()
    linkedList2 = LinkedList()

    # Measure time for inserting 50,000 random numbers at the beginning of linkedList1
    start_time = time.time()
    for _ in range(50000):
        linkedList1.insert_at_beginning(random.randint(1, 1000))
    print(f"Time to insert 50,000 nodes at the beginning: {time.time() - start_time} seconds")

    # Measure time for inserting 50,000 random numbers at the end of linkedList2
    start_time = time.time()
    for _ in range(50000):
        linkedList2.insert_at_end(random.randint(1, 1000))
    print(f"Time to insert 50,000 nodes at the end: {time.time() - start_time} seconds")

    # Measure time for deleting nodes from the beginning of linkedList1
    start_time = time.time()
    linkedList1.delete_from_beginning()
    print(f"Time to delete nodes from beginning: {time.time() - start_time} seconds")

    # Measure time for deleting nodes from the end of linkedList2
    start_time = time.time()
    linkedList2.delete_from_end()
    print(f"Time to delete nodes from end: {time.time() - start_time} seconds")

# Run the performance test
performance_test()
