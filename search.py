#!python

names = ['Alex', 'Brian','Julia', 'Kojin','Nabil',  'Nick', 'Winnie',   ]


def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Stephan github was a guide to this
    #Step 1: check to see if len(array)==0 and trhow if it is
    if len(array) == 0:
        return {'Message:','Array has no items'}
    #Step 2: Check to see if array[0] == 'item' and return index if it is
    else:
        if array[index] == item:
            return index
        #Step 3: itterate over the array until we fidn the 'item'
        elif index < len(array)-1:
            index += 1
            return linear_search_recursive(array, item, index)
        else:
            return None
    #Step 4: if not found, return "item not fund"


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # Help credit == Stephan
    if len(array) == 0:
        return None

    # Sets search windows
    left = 0
    right = len(array) - 1
    #Set local variables
    isFound = False
    result = None

    # start While loop
    while isFound == False:
                #Modifies search window
        middle_index = (left + right) // 2
        middle_value = array[middle_index]
        #condition if no result is found
        if left == right:
            if array[left] == item:
                result = left
                isFound = True
                continue
            return None
        # looks for item and modifies as needed
        if middle_value == item:
            result = middle_index
            isFound = True
        elif middle_value > item:
            right = middle_index - 1
        elif middle_value < item:
            left = middle_index + 1

    return result



def binary_search_recursive(array, item, left=None, right=None):
    if len(array) == 0:
        return None
        #Window
    if left == None:
        left = 0
        right = len(array)-1
        #Escape clause for if we searched everything
    if left > right:
        return None
        #Window
    middle_index = (left + right) // 2
    middle_value = array[middle_index]

    if item == middle_value:
        return middle_index

    elif item > middle_value:
        left = middle_index + 1

    elif item < middle_value:
        right = middle_index -1

    return binary_search_recursive(array, item, left, right)






if __name__ == '__main__':
    result = binary_search_recursive(names, 'Nick')
    print(result)
