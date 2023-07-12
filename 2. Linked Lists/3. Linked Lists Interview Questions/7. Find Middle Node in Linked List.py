# Interview Question #7
#
# Suppose we have a standard linked list. Construct an in-place
# (without extra memory) algorithm that's able to find the middle node!

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

    # O(N) linear running time complexity
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

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

    linked_list.insert_start(10)
    linked_list.insert_start(20)
    linked_list.insert_start(30)
    linked_list.insert_start(40)

    print(linked_list.get_middle_node().data)
