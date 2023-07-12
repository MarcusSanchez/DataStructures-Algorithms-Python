class Node:

    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None
        self.height = 0

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


class AVLTree:

    def __init__(self):
        self.root = None

    def remove(self, data):
        if self.root:
            self.__remove_node(data, self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.__insert_node(data, self.root)

    def __insert_node(self, data, node):
        # we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                self.__insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                node.height = max(self.__calculate_height(node.left_node), self.__calculate_height(node.right_node)) + 1
        # we have to visit the right subtree
        else:
            if node.right_node:
                self.__insert_node(data, node.right_node)
            else:
                node.right_node = Node(data, node)
                node.height = max(self.__calculate_height(node.left_node), self.__calculate_height(node.right_node)) + 1

        self.__handle_violation(node)

    def __handle_violation(self, node):

        while node is not None:
            node.height = max(self.__calculate_height(node.left_node), self.__calculate_height(node.right_node)) + 1
            self.__violation_helper(node)
            node = node.parent

    def __remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.__remove_node(data, node.left_node)
        elif data > node.data:
            self.__remove_node(data, node.right_node)
        else:

            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

                self.__handle_violation(parent)

            elif node.left_node is None and node.right_node is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

                self.__handle_violation(parent)

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

                self.__handle_violation(parent)

            else:
                print('Removing node with two children....')

                predecessor = self.__get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.__remove_node(data, predecessor)

    def __get_predecessor(self, node):
        if node.right_node:
            return self.__get_predecessor(node.right_node)

        return node

    def __violation_helper(self, node):

        balance = self.__calculate_balance(node)

        # OK, we know the tree is left heavy BUT it can be left-right heavy or left-left heavy
        if balance > 1:

            # left right heavy situation: left rotation on parent + right rotation on grandparent
            if self.__calculate_balance(node.left_node) < 0:
                self.__rotate_left(node.left_node)

            # this is the right rotation on grandparent ( if left-left heavy, that's single right rotation is needed
            self.__rotate_right(node)

        # OK, we know the tree is right heavy BUT it can be left-right heavy or right-right heavy
        if balance < -1:

            # right - left heavy, so we need a right rotation  before left rotation
            if self.__calculate_balance(node.right_node) > 0:
                self.__rotate_right(node.right_node)

            # left rotation
            self.__rotate_left(node)

    @staticmethod
    def __calculate_height(node):

        if node is None:
            return -1

        return node.height

    def __calculate_balance(self, node):

        if node is None:
            return 0

        return self.__calculate_height(node.left_node) - self.__calculate_height(node.right_node)

    def traverse(self):
        if self.root is not None:
            yield from self.__traverse_in_order(self.root)

    def __traverse_in_order(self, node):
        if node.left_node is not None:
            yield from self.__traverse_in_order(node.left_node)

        yield node.data

        if node.right_node is not None:
            yield from self.__traverse_in_order(node.right_node)

    def __rotate_right(self, node):
        #              left_left             |              left_right
        #       (5)                4         |      (5)              (5)             4
        #     4       ->       3      (5)    |   3         ->      4        ->   3      (5)
        #   3                                |      4           3
        print("Rotating to the right on node ", node.data)

        # vars are relative to the node pre-operation
        left_child = node.left_node
        left_childs_right_child = left_child.right_node

        # point left child right node to the node in question
        left_child.right_node = node
        # point the node's left node to the left child's right child
        node.left_node = left_childs_right_child

        # if the left child has a right child, we must assign its parent to be the node
        if left_childs_right_child is not None:
            left_childs_right_child.parent = node

        # now we have to change the node's parent to the left child, and the left child's
        # parent to the node's original parent
        node.parent, left_child.parent = left_child, node.parent

        # making parent point to rotated node:
        # left child
        if left_child.parent is not None and left_child.parent.left_node == node:
            left_child.parent.left_node = left_child

        # right child
        if left_child.parent is not None and left_child.parent.right_node == node:
            left_child.parent.right_node = left_child

        # if we shifted the root right, we must reassign the root to the new root
        if node == self.root:
            self.root = left_child

        # update the heights of the nodes
        node.height = max(self.__calculate_height(node.left_node),
                          self.__calculate_height(node.right_node)) + 1

        left_child.height = max(self.__calculate_height(left_child.left_node),
                                self.__calculate_height(left_child.right_node)) + 1

    def __rotate_left(self, node):
        #              right_right         |              right_left
        #  (5)                  6          |       (5)             (5)                    6
        #     6       ->   (5)     7       |           7      ->        6        ->   (5)    7
        #       7                          |         6                     7

        print("Rotating to the left on node ", node.data)

        # vars are relative to the node pre-operation
        right_child = node.right_node
        right_childs_left_child = right_child.left_node

        # point right child left node to the node in question
        right_child.left_node = node
        # point the node's right node to the right child's left child
        node.right_node = right_childs_left_child

        # if the right child has a left child, we must assign its parent to be the node
        if right_childs_left_child is not None:
            right_childs_left_child.parent = node

        # now we have to change the node's parent to the right child, and the right child's
        # parent to the node's original parent
        node.parent, right_child.parent = right_child, node.parent

        # making parent point to rotated node:
        # right child
        if right_child.parent is not None and right_child.parent.left_node == node:
            right_child.parent.left_node = right_child

        # left child
        if right_child.parent is not None and right_child.parent.right_node == node:
            right_child.parent.right_node = right_child

        # if we shifted the root left, we must reassign the root to the new root
        if node == self.root:
            self.root = right_child

        # update the heights of the nodes
        node.height = max(self.__calculate_height(node.left_node),
                          self.__calculate_height(node.right_node)) + 1

        right_child.height = max(self.__calculate_height(right_child.left_node),
                                 self.__calculate_height(right_child.right_node)) + 1

    def display(self):
        if self.root is not None:
            node = self.root
            node.display()


if __name__ == '__main__':
    ...
