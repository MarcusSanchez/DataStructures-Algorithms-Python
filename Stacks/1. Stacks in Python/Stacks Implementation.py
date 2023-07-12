# LIFO: last item we insert is the first item we remove

class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    # insert item into stack // O(1)
    def push(self, data):
        self.stack.append(data)
        self.size += 1

    # remove and return last item we have inserted (LIFO) // O(1)
    def pop_last(self):
        if self.stack_size() < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        self.size -= 1
        return data

    # returns last item without removing it // O(1)
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return self.size


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f'Size: {stack.stack_size()}\n')
print(f'Popped Item: {stack.pop_last()}')
print(f'Size: {stack.stack_size()}\n')
print(f'Peeked Item: {stack.peek()}')
print(f'Size: {stack.stack_size()}\n')
print(stack.stack)
print('\n')
print(stack.stack)
print(stack.is_empty())
print(stack.stack_size())



