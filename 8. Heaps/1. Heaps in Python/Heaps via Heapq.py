import heapq

# it is the min heap implementation
# heap = [4, 7, 3, -2, 1, 0]
#
# heapq.heapify(heap)
#
# print(heap)

nums = [4, 7, 3, -2, 1, 0]
heap = []

for value in nums:
    heapq.heappush(heap, value)

print(heap)

for i in heap[:]:
    print(heapq.heappop(heap))
