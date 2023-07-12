class Heap:

    def __init__(self):
        self.heap = []

    def transform(self):
        for i in range((len(self.heap) - 2) // 2, -1, -1):
            self.__fix_down_minimum(i)

    def __fix_down_minimum(self, index):

        index_left = 2 * index + 1
        index_right = 2 * index + 2

        largest_index = index

        if index_left < len(heap.heap) and self.heap[index_left] < self.heap[index]:
            largest_index = index_left

        if index_right < len(heap.heap) and self.heap[index_right] < self.heap[largest_index]:
            largest_index = index_right

        if index != largest_index:
            self.heap[index], self.heap[largest_index] = self.heap[largest_index], self.heap[index]
            self.__fix_down_minimum(largest_index)


if __name__ == '__main__':

    heap = Heap()
    heap.heap = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    heap.transform()
    print(heap.heap)
