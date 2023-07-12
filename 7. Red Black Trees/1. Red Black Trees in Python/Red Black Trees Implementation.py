
class Color:
    RED = 1
    BLACK = 2


class Node:

    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.color = color

    def display(self):
        lines, *_ = self.__display_aux()
        for line in lines:
            print(line)

    def __display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_node is None and self.left_node is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left_node child.
        if self.right_node is None:
            lines, n, p, x = self.left_node.__display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right_node child.
        if self.left_node is None:
            lines, n, p, x = self.right_node.__display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left_node, n, p, x = self.left_node.__display_aux()
        right_node, m, q, y = self.right_node.__display_aux()
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


class RedBlackTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            self.__settle_violation(self.root)
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, node):

        if data < node.data:
            if node.left_node is not None:
                self.__insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                self.__settle_violation(node.left_node)
        else:
            if node.right_node is not None:
                self.__insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                self.__settle_violation(node.right_node)

    def __settle_violation(self, node):
        while node != self.root and self.__is_red(node) and self.__is_red(node.parent):
            parent_node = node.parent
            grandpa_node = parent_node.parent

            if grandpa_node is None:
                return

            # parent is a left child of it's parent (so the grandpa)
            if parent_node == grandpa_node.left_node:
                uncle_node = grandpa_node.right_node

                # case 1: and case 4: RECOLORING
                if uncle_node is not None and self.__is_red(uncle_node):
                    print(f'Re-coloring node {grandpa_node.data} to RED')
                    grandpa_node.color = Color.RED
                    print(f'Re-coloring node {parent_node.data} to BLACK')
                    parent_node.color = Color.BLACK
                    uncle_node.color = Color.BLACK
                    node = grandpa_node
                else:
                    # case 2: uncle node is black and node is a right child
                    if node == parent_node.right_node:
                        self.__rotate_left(parent_node)
                        node, parent_node = parent_node, node.parent

                    # case 3: rotation on the grandparent and the parent and the grandparent switch colors
                    parent_node.color = Color.BLACK
                    grandpa_node.color = Color.RED
                    print(f'Re-color {parent_node.data} to BLACK')
                    print(f'Re-color {grandpa_node.data} to RED')
                    self.__rotate_right(grandpa_node)
            else:

                uncle_node = grandpa_node.left_node

                if uncle_node and self.__is_red(uncle_node):
                    # case 1 and case 4
                    print(f'Re-coloring node {grandpa_node.data} to RED')
                    grandpa_node.color = Color.RED
                    print(f'Re-coloring node {parent_node.data} to BLACK')
                    parent_node.color = Color.BLACK
                    uncle_node.color = Color.BLACK
                    node = grandpa_node

                else:
                    # case 2: uncle node is black and node is a right child
                    if node == parent_node.left_node:
                        self.__rotate_right(parent_node)
                        node = parent_node
                        parent_node = node.parent

                    # case 3
                    parent_node.color = Color.BLACK
                    grandpa_node.color = Color.RED
                    print(f'Re-coloring {parent_node.data} to BLACK')
                    print(f'Re-coloring {grandpa_node.data} to RED')
                    self.__rotate_left(grandpa_node)
        if self.__is_red(self.root):
            print('Re-coloring root to BLACK')
            self.root.color = Color.BLACK

    @staticmethod
    def __is_red(node):
        if node is None:
            return False

        return node.color == Color.RED

    @staticmethod
    def __is_black(node):
        if node is None:
            return True

        return node.color == Color.BLACK

    def traverse(self):

        if self.root is not None:
            self.__in_order_traversal(self.root)

    def __in_order_traversal(self, node):
        if node.left_node:
            self.__in_order_traversal(node.left_node)

        print(node.data)

        if node.right_node is not None:
            self.__in_order_traversal(node.right_node)

    def __rotate_right(self, node):
        print("Rotating to the right on node", node.data)

        left_child = node.left_node
        left_childs_right_child = left_child.right_node

        left_child.right_node = node
        node.left_node = left_childs_right_child

        if left_childs_right_child is not None:
            left_childs_right_child.parent = node

        node.parent, left_child.parent = left_child, node.parent

        if left_child.parent is not None and left_child.parent.left_node == node:
            left_child.parent.left_node = left_child

        if left_child.parent is not None and left_child.parent.right_node == node:
            left_child.parent.right_node = left_child

        if node == self.root:
            self.root = left_child

    def __rotate_left(self, node):

        print("Rotating to the left on node", node.data)

        right_child = node.right_node
        right_childs_left_child = right_child.left_node

        right_child.left_node = node
        node.right_node = right_childs_left_child

        if right_childs_left_child is not None:
            right_childs_left_child.parent = node

        node.parent, right_child.parent = right_child, node.parent

        if right_child.parent is not None and right_child.parent.left_node == node:
            right_child.parent.left_node = right_child

        if right_child.parent is not None and right_child.parent.right_node == node:
            right_child.parent.right_node = right_child

        if node == self.root:
            self.root = right_child

    def display(self):
        if self.root is not None:
            node = self.root
            node.display()


if __name__ == '__main__':
    rbt = RedBlackTree()
    rbt.insert(32)
    rbt.insert(10)
    rbt.insert(55)
    rbt.insert(1)
    rbt.insert(19)
    rbt.insert(79)
    rbt.insert(16)
    rbt.insert(23)
    rbt.insert(12)
    rbt.display()
