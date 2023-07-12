# Interview Question #3

# Our task is to design an efficient algorithm to reverse a given integer.
# For example if the input of the algorithm is 1234 then the output should be 4321.

def reverseInteger(n):
    reverse = 0

    while n > 0:
        remainder = n % 10
        reverse = reverse * 10 + remainder
        n = n // 10

    return reverse


if __name__ == '__main__':
    print(reverseInteger(7654))


