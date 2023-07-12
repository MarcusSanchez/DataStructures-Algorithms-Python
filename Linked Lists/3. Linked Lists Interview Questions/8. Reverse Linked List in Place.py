# Interview Question #8
#
# Construct an in-place algorithm to reverse a linked list!

class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # O(N) running time complexity
    def reverse(self):
        current_node = self.head
        previous_node = None

        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head

            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node

    def size_of_list(self):
        return self.num_of_nodes

    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

    def remove(self, data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node


if __name__ == '__main__':

    linked_list = LinkedList()

    insertionList = [12, 122, 3, 31, 10, 11]

    for i in insertionList:
        linked_list.insert_start(i)

    linked_list.traverse()
    linked_list.reverse()
    print('reverse list')
    linked_list.traverse()
