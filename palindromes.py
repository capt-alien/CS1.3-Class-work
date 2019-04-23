#!python
import re

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)

def is_palindrome_easy(text):
    # Take text make it all lowercase and filter out non-letters using re
    lower= text.lower()
    text_list = re.findall('[a-z]', lower)
    print(text_list)
    print(text_list[::-1])
    if text_list == text_list[::-1]:
        return True


def is_palindrome_iterative(text):
    # Take text make it all lowercase and filter out non-letters using re
    lower= text.lower()
    # Use RE to filter out non alpha char and split into list
    text_list = re.findall('[a-z]', lower)
    # Create search windows
    left = 0
    right = len(text_list)-1
    while left<right:
        if text_list[left] != text_list[right]:
            return False
            break
        else:
            left += 1
            right -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
    # if sting is ''
    if len(text_list)==0:
        return True
    # If first round
    if left == None:
        left = 0
        right = len(text_list)-1
        lower= text.lower()
        text_list = re.findall('[a-z]', lower)
    # escape clause if true
    if text_list[left] != text_list[right]:
        return False
    elif left >= right:
        return True
    else:
        return is_palindrome_recursive(text, left + 1 , right-1)



def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
