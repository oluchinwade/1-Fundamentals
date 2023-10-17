# STEP 1, Create Node class
# In this step, we define a Node class that represents a single element in our linked list.
# Each Node has a 'value' to store the data, and a 'next' attribute to point to the next Node in the list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# STEP 2, Create LinkedList Class
# We create a LinkedList class to manage the linked list data structure.
# It has an initial 'head' attribute which is the starting point of the list (initialized as None).
class LinkedList:
    def __init__(self):
        self.head = None

# STEP 3, Add Node to LinkedList
# In this step, we define the 'insert' method within the LinkedList class.
# This method allows us to add a new Node with a given 'value' to the linked list.
    def insert(self, value):
        new_node = Node(value)
        # Check if the list is empty (head is None)
        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return
        # Traverse the list to find the last Node and append the new Node to it
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node
        print("Appended new Node with value:", node.next.value)

# Create an instance of the LinkedList class
linked_list = LinkedList()

# STEP 4, Print Linked List
# We insert nodes with values '1st' and '2nd' into the linked list and print appropriate messages.
linked_list.insert("1st")
linked_list.insert("2nd")
