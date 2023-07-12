# Interview Question #4

# Construct an algorithm to check whether two words (or phrases) are anagrams or not!

# For example: restful and fluster

def is_anagram(s, s2):
    # check lengths first to see if they differ
    if len(s) != len(s2):
        return False

    # sort letters to check letters with the same indexes
    s = sorted(s)
    s2 = sorted(s2)

    # check letters with same indexes
    for i in range(len(s)):
        if s[i] != s2[i]:
            return False

    return True


if __name__ == '__main__':
    print(is_anagram('fluster', 'restful'))

