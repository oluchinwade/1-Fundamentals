class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
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
    def prepend(self, value):
        new_value = Node(value)
        if self.head is None:
            self.head = new_value
            print(f"Head Node is: {self.head.value}")
            return
        elif self.head is not None:
            new_value.next = self.head
            self.head = new_value
            print("Prepended new Head Node with value:", self.head.value)
            print("Node following Head is:", self.head.next.value)


linked_list = LinkedList()


linked_list.prepend("1st")
linked_list.prepend("2nd")
