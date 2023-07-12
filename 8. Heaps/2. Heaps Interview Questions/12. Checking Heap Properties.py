# Interview question #12 - checking heap properties

# We have seen how to implement min (and max) heaps from scratch.
# Your task is to check whether a list contains a valid min heap or not.

#     def is_min_heap(heap):
#         ...

# The heap is a list data structure containing integers.

# Hint: you just have to check the heap properties 
# (in a min heap the parent is smaller than the children)

import heapq as hq


# my answer
def is_min_heap(heap):
    for i in range(len(heap)):
        try:
            if heap[i] > heap[2*i + 1] or heap[i] > heap[2*i + 2]:
                return False
        except IndexError:
            return True

    return True


# correct answer
def is_min_heap2(heap):

    # there is no need to check the leaf nodes
    num_items = (len(heap) - 2) // 2

    for i in range(num_items + 1):
        # we have to check the heap property
        # the parent must be smaller than the children
        if heap[i] > heap[2*i + 1] or heap[i] > heap[2*i + 2]:
            return False

    return True


if __name__ == '__main__':
    list1 = [47, 1, 5, 8, 3, 2, 9, 4, 3, 500, -66]
    list2 = [47, 1, 5, 8, 3, 2, 9, 4, 3, 500, -66]
    list3 = [1, 2, 3, 5, 4, -100]

    hq.heapify(list2)

    print(is_min_heap(list1))
    print(is_min_heap(list2))
    print(is_min_heap(list3))

    print(list1)
    print(list2)
    print(list3)

    print(is_min_heap2(list1))
    print(is_min_heap2(list2))
    print(is_min_heap2(list3))

