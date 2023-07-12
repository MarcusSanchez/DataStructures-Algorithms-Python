# Given n non-negative integers representing an elevation map where the width of each bar is 1.
# Compute how much water it can trap after raining!

# Here the elevation map (the input for the algorithm) is [4,1,3,1,5] and
# the output is the total units of trapped rain water - which is 7.

def rainWaterProblem(heights):
    if len(heights) < 3:
        return 0

    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    # dealing with the left max value
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i - 1], heights[i - 1])

    # dealing with the right max values
    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i + 1])

    # consider all items in O(N) and sum up the trapped water units
    trapped = 0

    for i in range(1, len(heights) - 1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped += min(left_max[i], right_max[i] - heights[i])

    print(left_max)
    print(right_max)
    return trapped


if __name__ == '__main__':
    print(rainWaterProblem([1, 0, 0, 18, 0, 0, 20]))


            