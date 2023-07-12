# Interview Question #10

# Write an efficient algorithm that's able to compare two binary search trees.
# The method returns true if the trees are identical
# (same topology with the same values in the nodes)
# Otherwise it returns False.

class TreeComparator:

    def compare(self, node1, node2):

        # check the base-case (so these node1 and node2 may be the nodes
        # of a leaf node)
        # node1 may be a None or node2 may be a None
        if node1 is None or node2 is None:
            return node1 == node2

        # we have to check the values in the nodes
        if node1.data != node2.data:
            return False

        # check all the left and right subtrees (children) recursively
        return self.compare(node1.left_node, node2.left_node) and self.compare(node1.right_node, node2.right_node)


class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
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
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, node):
        if data < node.data:
            if node.left_node is not None:
                self.__insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
        else:
            if node.right_node is not None:
                self.__insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)

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

    def __traverse_in_order(self, node):
        if node.left_node is not None:
            self.__traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node is not None:
            self.__traverse_in_order(node.right_node)

    def remove(self, data):
        if self.root is not None:
            self.__remove_node(data, self.root)

    def __remove_node(self, data, node):
        if node is None:
            return

        if data < node.data:
            self.__remove_node(data, node.left_node)
        elif data > node.data:
            self.__remove_node(data, node.right_node)
        else:
            if node.left_node is None and node.right_node is None:
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                del node

            elif node.left_node is None and node.right_node is not None:
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = node.right_node

                node.right_node.parent = parent

                del node

            elif node.right_node is None and node.left_node is not None:
                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = node.left_node
                if parent is not None and parent.right_node == node:
                    parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            else:
                predecessor = self.__get_predecessor(node.left_node)

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

    bst1 = BinarySearchTree()
    bst1.insert(2863)
    bst1.insert(3375)
    bst1.insert(949)
    bst1.insert(301)
    bst1.insert(284)
    bst1.insert(731)
    bst1.insert(1433)
    bst1.insert(1297)
    bst1.insert(1055)
    bst1.insert(2666)
    bst1.insert(1904)
    bst1.insert(1446)
    bst1.insert(-44)
    bst1.insert(728)
    bst1.insert(6)
    bst1.insert(3077)
    bst1.insert(1859)
    bst1.insert(-12)
    bst1.insert(4930)
    bst1.insert(3134)
    bst1.insert(3789)
    bst1.insert(3436)
    bst1.insert(3364)
    bst1.insert(4845)
    bst1.insert(4354)
    bst1.insert(4389)
    bst1.insert(-4430)
    bst1.insert(4634)
    bst1.insert(3981)
    bst1.insert(9)
    bst1.insert(5866)
    bst1.insert(5222)
    bst1.insert(4849)
    bst1.insert(4888)
    bst1.insert(4920)
    bst1.insert(4900)

    bst2 = BinarySearchTree()
    bst2.insert(2863)
    bst2.insert(3375)
    bst2.insert(284)
    bst2.insert(949)
    bst2.insert(301)
    bst2.insert(731)
    bst2.insert(1433)
    bst2.insert(1297)
    bst2.insert(1055)
    bst2.insert(2666)
    bst2.insert(1904)
    bst2.insert(1446)
    bst2.insert(-44)
    bst2.insert(728)
    bst2.insert(6)
    bst2.insert(3077)
    bst2.insert(-12)
    bst2.insert(4930)
    bst2.insert(3134)
    bst2.insert(3789)
    bst2.insert(3436)
    bst2.insert(3364)
    bst2.insert(4845)
    bst2.insert(4354)
    bst2.insert(4389)
    bst2.insert(-4430)
    bst2.insert(4634)
    bst2.insert(3981)
    bst2.insert(1859)
    bst2.insert(5866)
    bst2.insert(5222)
    bst2.insert(4849)
    bst2.insert(4888)
    bst2.insert(4920)
    bst2.insert(4900)
    bst2.insert(9)

    comparator = TreeComparator()
    print(comparator.compare(bst1.root, bst2.root))