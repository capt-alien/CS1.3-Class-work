import sys

#Create some helper functions
def z_pattern(text):
    """Returns bollean if patteren is empty string"""
    pat_size = len(text)
    if pat_size ==0:
        return True
    else:
        return False

def find_all_indexes(text, pattern):
    # time complexity: O(n) due to for loop.
    #Space complexity: O(n^2) due to new lists
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    indicies = []
    if z_pattern(text):
        return indicies
        # While Loop
    for i in range(len(text)):
        right = (i +len(pattern))
        if text[i:right] == pattern:
            indicies.append(i)
    return indicies

def contains(text, pattern):
    # time complexity: O(n) due to for loop in find_all_indexes
    #Space complexity: O(n^2) due to new lists in find_all_indexes
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if find_all_indexes(text, pattern) != []:
        return True
    else:
        return False
    # code from before refactor:
    # if z_pattern(pattern):
    #     return True
    #     # While Loop
    # for i in range(0,len(text)-len(pattern)+1):
    #     right = (i +len(pattern))
    #     if text[i:right] == pattern:
    #         return True
    # else:
    #     return False


def find_index(text, pattern):
    # time complexity: O(n) due to for loop in find_all_indexes
    #Space complexity: O(n^2) due to new lists in find_all_indexes
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    first=find_all_indexes(text, pattern)
    if len(first)>0:
        return first[0]
    else:
        return None
    #Code from before refactor:
    # if z_pattern(pattern):
    #     return 0
    #     # While Loop
    # for i in range(len(text)):
    #     right = (i +len(pattern))
    #     if text[i:right] == pattern:
    #         return i


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
