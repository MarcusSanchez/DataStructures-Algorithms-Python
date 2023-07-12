# I ---------------------------------------------------------
class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        # crucial to remove function
        self.parent = parent

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        if self.right_node is None and self.left_node is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if self.right_node is None:
            lines, n, p, x = self.left_node._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left_node is None:
            lines, n, p, x = self.right_node._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left_node, n, p, x = self.left_node._display_aux()
        right_node, m, q, y = self.right_node._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left_node += [n * ' '] * (q - p)
        elif q < p:
            right_node += [m * ' '] * (p - q)
        zipped_lines = zip(left_node, right_node)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:

    def __init__(self):
        # we can access the root node exclusively
        self.root = None

    def insert(self, data):
        # this is the first node in the binary search tree
        if self.root is None:
            self.root = Node(data)
            # the BST is not empty
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_node is not None:
                # the left node exists (so we keep going)
                self.__insert_node(data, node.left_node)
            else:
                # there is no left child (so we create one)
                node.left_node = Node(data, node)
        # we have to go to the right subtree
        else:
            if node.right_node is not None:
                self.__insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

# II --------------------------------------------------------

    def get_min(self):
        if self.root is not None:
            return self.__get_minimum_value(self.root)

    def __get_minimum_value(self, node):

        if node.left_node is not None:
            return self.__get_minimum_value(node.left_node)

        return node.data

    def get_max(self):
        if self.root is not None:
            return self.__get_maximum_value(self.root)

    def __get_maximum_value(self, node):

        if node.right_node is not None:
            return self.__get_maximum_value(node.right_node)

        return node.data

    def traverse(self):
        if self.root is not None:
            self.__traverse_in_order(self.root)

    # O(N) running time complexity
    def __traverse_in_order(self, node):
        if node.left_node is not None:
            self.__traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node is not None:
            self.__traverse_in_order(node.right_node)

# III-------------------------------------------------------

    def remove(self, data):
        if self.root is not None:
            self.__remove_node(data, self.root)

    def __remove_node(self, data, node):
        # we have to find the node we want to remove
        if node is None:
            return

        if data < node.data:
            self.__remove_node(data, node.left_node)
        elif data > node.data:
            self.__remove_node(data, node.right_node)
        else:
            # we have found the node we want
            # there are three options
            # LEAF NODE CASE
            if node.left_node is None and node.right_node is None:
                # print(f'Removing a leaf node...{node.data}')
                parent = node.parent
                # this is the left leaf node
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                # this is the right leaf node
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                del node

            # WHEN THERE IS A SINGLE CHILD
            elif node.left_node is None and node.right_node is not None:
                # print(f'Removing a node with single right child...')
                parent = node.parent

                # left single child
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                # right single child
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                # the root node is the one we want to remove
                if parent is None:
                    self.root = node.right_node

                node.right_node.parent = parent

                del node

            elif node.right_node is None and node.left_node is not None:
                # print(f'Removing a node with single left child...')
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            # REMOVE NODE WITH TWO CHILDREN
            else:
                # print(f'Removing node with two children...')
                predecessor = self.__get_predecessor(node.left_node)

                # swap the node and predecessor(node.right_node)
                predecessor.data, node.data = node.data, predecessor.data

                self.__remove_node(data, predecessor)

    def __get_predecessor(self, node):
        if node.right_node is not None:
            return self.__get_predecessor(node.right_node)

        return node

    def display(self):
        if self.root is not None:
            node = self.root
            node.display()


if __name__ == '__main__':

    bst = BinarySearchTree()
    # for i in range(27):
    #     bst.insert(random.randint(1, 5000))
    bst.insert(2863)
    bst.insert(3375)
    bst.insert(284)
    bst.insert(949)
    bst.insert(301)
    bst.insert(731)
    bst.insert(1433)
    bst.insert(1297)
    bst.insert(1055)
    bst.insert(2666)
    bst.insert(1904)
    bst.insert(1446)
    bst.insert(-44)
    bst.insert(728)
    bst.insert(6)
    bst.insert(3077)
    bst.insert(-12)
    bst.insert(4930)
    bst.insert(3134)
    bst.insert(3789)
    bst.insert(3436)
    bst.insert(3364)
    bst.insert(4845)
    bst.insert(4354)
    bst.insert(4389)
    bst.insert(-4430)
    bst.insert(4634)
    bst.insert(3981)
    bst.insert(1859)
    bst.insert(9)
    bst.insert(5866)
    bst.insert(5222)
    bst.insert(4849)
    bst.insert(4888)
    bst.insert(4920)
    bst.insert(4900)
    bst.display()
    bst.remove(4930)
    print('')
    bst.display()
    print(f'MAX: {bst.get_max()}')
    print(f'MIN: {bst.get_min()}')
    bst.traverse()














