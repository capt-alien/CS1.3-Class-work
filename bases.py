#!python

## All your base are with us

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    digits = digits[::-1]
    exponent = 0
    total = 0
    #run the loop in reverse order adding up the results.
    for i in range(len(digits)):
        #multiply base by power i
        adder = string.hexdigits.find(digits[i])*(base**i)
        #add result to total
        total += adder
    return total

    # assert encode(15, 2) == '1111'

def encode(number, base):
    #Got Help from Marrianna
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    assert number >= 0, 'number is negative: {}'.format(number)
    # Convert number string into a reversed list
    e_string = ''
    current_base = 0
    looper = False
    base_list = []
    while looper is False:
        base_value = base**current_base
        print(base_value, current_base)
        if base_value < number:
            base_list.insert(0,current_base)
            current_base += 1
        elif base_value == number:
            base_list.insert(0,current_base)
            looper = True
        else:
            looper = True

    for power in base_list:
        base_value = base**power
        limit = int(number/base_value)
        number -= base_value * limit
        e_string += string.printable[limit]
    return e_string

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    decoded = decode(digits, base1)
    encoded = encode(decoded, base2)
    return encoded



def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    # print(encode(12, 2))
