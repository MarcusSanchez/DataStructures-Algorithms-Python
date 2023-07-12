# Dutch national flag problem overview

# The problem is that we want to sort a T[] one-dimensional array of integers in O(N)
# running time - and without any extra memory. The array can contain values: 0, 1 and 2
# (check out the theoretical section for further information).

def dutchFlagProblem(nums, pivot=1):
    i = 0
    j = 0
    k = len(nums) - 1

    while j <= k:
        # item is 0
        if nums[j] < pivot:
            swap(nums, i, j)
            i += 1
            j += 1
        # item is 2
        elif nums[j] > pivot:
            swap(nums, j, k)
            k -= 1
        # item is 1
        else:
            j += 1

    return nums


def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1]


if __name__ == '__main__':
    print(dutchFlagProblem([0, 1, 2, 2, 1, 0, 0, 2, 2, 2, 1, 1, 2, 2, 0, 0, 0]))
