class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linked_list:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_linked_list(self):
        if not self.head:
            print("None")
            return

        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

    def prepend(self, data):
        new_node = Node(data)
        temp = self.head
        self.head = new_node
        self.head.next = temp

    def insert_at_index(self, index, data):
        new_node = Node(data)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < index - 1:
            count += 1
            current = current.next

        new_node.next = current.next
        current.next = new_node


my_list = Linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.insert_at_index(2, 5)
my_list.prepend(4)
my_list.print_linked_list()
