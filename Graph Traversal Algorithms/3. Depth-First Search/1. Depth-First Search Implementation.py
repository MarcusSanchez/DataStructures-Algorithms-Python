class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False


def depth_first_search(starting_node):

    # we need a LIFO: last item we insert is the first item we take out
    stack = [starting_node]
    starting_node.visited = True

    # let's iterate until the stack becomes empty
    while stack:

        # pop() returns with the last item we inserted // O(1)
        actual_node = stack.pop()

        yield actual_node.name
        for n in actual_node.adjacency_list:
            # if the node has not been visited so far
            if n.visited is False:
                # insert item into the stack
                n.visited = True
                stack.append(n)


if __name__ == '__main__':

    # we can create the nodes or vertices
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    # we have to handle the neighbors
    # node1.adjacency_list.append(node2)  #      2 - 4 - 5
    # node1.adjacency_list.append(node3)  # 1  <
    # node2.adjacency_list.append(node4)  #      3
    # node4.adjacency_list.append(node5)  #

    # # we have to handle the neighbors
    node1.adjacency_list.append(node2)  #  1 - 2 - 3
    node2.adjacency_list.append(node3)  #  |    \ /
    node2.adjacency_list.append(node4)  #  5     4
    node3.adjacency_list.append(node4)  #
    node5.adjacency_list.append(node1)  #

    node2.adjacency_list.append(node1)
    node3.adjacency_list.append(node2)
    node4.adjacency_list.append(node2)
    node4.adjacency_list.append(node3)
    node1.adjacency_list.append(node5)

    # run the DFS
    print(list(depth_first_search(node5)))

