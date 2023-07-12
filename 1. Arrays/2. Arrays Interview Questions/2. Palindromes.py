# Interview Question #2
# "A palindrome is a string that reads the same forward and backward"

# For example: radar or madam

# Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!


# it has O(s) so basically linear running time complexity as far as the number of letters in the string is concerned.
def isPalindrome(s):
    original_string = s
    reversed_string = reverseData(s)
    if original_string == reversed_string:
        return True

    return False


def reverseData(data):
    data = list(data)
    print(data)
    start_index = 0
    end_index = len(data) - 1
    while end_index > start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index += 1
        end_index -= 1

    return ''.join(data)


if __name__ == '__main__':
    print(isPalindrome('racecar'))
