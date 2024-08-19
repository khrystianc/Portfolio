def conv_num(num_str):
    """
    This function takes in a string and converts it into a base 10 number,
    and returns it.
    """
    # Make sure it is not an empty string
    if not isinstance(num_str, str) or not num_str:
        return None

    num_str = num_str.strip().lower()

    # Check if the string is positive or has a negative sign
    if num_str.startswith('-'):
        sign = -1
        num_str = num_str[1:]
    else:
        sign = 1

    if num_str.isdigit():
        # Handle integer strings
        return sign * conv_int(num_str)
    elif '.' in num_str:
        # Handle floating point strings
        if num_str.count('.') > 1 or not num_str.replace('.', '').isdigit():
            return None
        whole_part, decimal_part = num_str.split('.')
        return sign * (conv_int(whole_part) + conv_float(decimal_part))
    elif num_str.startswith('0x'):
        # Handle hexadecimal strings
        num_str = num_str[2:]
        if not num_str or not all(c.isdigit() or ('a' <= c <= 'f') for c in num_str):
            return None
        return sign * conv_hex(num_str)
    else:
        # Invalid format
        return None


def conv_int(num_str):
    # Function to convert string of an integer to an integer
    num = 0
    for i in num_str:
        if not i.isdigit():
            return None
        num = num * 10 + char_to_int(i)
    return num


def conv_float(num_str):
    # Convert string a decimal to a float value
    decimal = 0
    factor = 0.1
    for i in num_str:
        if not i.isdigit():
            return None
        decimal += factor * char_to_int(i)
        factor /= 10
    return decimal


def conv_hex(num_str):
    # Convert string of a hexadecimal number to int
    num = 0
    for i in num_str:
        if not i.isdigit() and not ('a' <= i <= 'f'):
            return None
        num = num * 16 + (char_to_int(i) if i.isdigit()
                          else ord(i) - ord('a') + 10)
    return num


def char_to_int(char):
    # Map a character digit to its integer value
    return ord(char) - ord('0')
