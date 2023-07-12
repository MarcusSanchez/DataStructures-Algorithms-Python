class Node:

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        
    def __repr__(self):
        return self.name


def breadth_first_search(start_node):
    # FIFO: first item we insert is the first one we take out
    queue = [start_node]
    start_node.visited = True

    # we keep iterating (considering the neighbors) until the queue becomes empty
    while queue:

        # remove and return the first item we have inserted into the list
        actual_node = queue.pop(0)
        print(actual_node.name)
        # let's consider the neighbors of the actual_node one by one
        for n in actual_node.adjacency_list:
            if n.visited is False:
                n.visited = True
                queue.append(n)


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

    # we have to handle the neighbors
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

    # run the BFS
    breadth_first_search(node3)
