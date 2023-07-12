# Interview Question #8
#
# The aim is to design an algorithm that can return the maximum item
# of a stack in O(1) running time complexity. We can use O(N) extra memory!
# Hint: we can use another stack to track the max item!
import random


class MaxStack:

    def __init__(self):
        # stack for the enqueue operation
        self.stack = []
        # stack for the dequeue operation
        self.max_stack = []

    def push(self, data):
        self.stack.append(data)

        # first item is the same in both stacks
        if len(self.stack) == 1:
            self.max_stack.append(data)
            return

        # if the item is the largest one so far: we insert it onto the stack.
        # stack[-1] is the peek operation: returns the last item we have inserted
        if data > self.max_stack[-1]:
            self.max_stack.append(data)
        else:
            # if not the largest one then we duplicate the largest one onto the max_stack
            self.max_stack.append(self.max_stack[-1])

    # getting items
    def pop_last(self):
        del self.max_stack[-1]
        return self.stack.pop()

    # max item is the last item we have inserted into the max_stack // O(N) running time
    def get_max(self):
        return self.max_stack[-1]


if __name__ == '__main__':
    max_stack = MaxStack()

    for i in range(10):
        max_stack.push(random.randint(1, 500))

    print(max_stack.get_max())
    print(max_stack.stack)
    print(max_stack.max_stack)
    max_stack.pop_last()
    max_stack.pop_last()
    max_stack.pop_last()
    max_stack.pop_last()
    max_stack.pop_last()
    max_stack.pop_last()
    max_stack.pop_last()
    max_stack.pop_last()
    max_stack.pop_last()
    print('\n')
    print(max_stack.stack)
    print(max_stack.max_stack)
    max_stack.get_max()

