def conv_num(num_str):
    if not isinstance(num_str, str) or not num_str:
        return None

    num_str = num_str.strip().lower()

    if num_str.startswith('-'):
        sign = -1
        num_str = num_str[1:]
    else:
        sign = 1

    if num_str.startswith('0x'):
        num_str = num_str[2:]
        if not all(c.isdigit() or ('a' <= c <= 'f') for c in num_str):
            return None
        return sign * conv_hex(num_str)
    elif '.' in num_str:
        if num_str.count('.') > 1 or not num_str.replace('.', '').isdigit():
            return None
        return sign * conv_float(num_str)
    elif num_str.isdigit():
        return sign * conv_int(num_str)
    else:
        return None


def conv_int(num_str):
    num = 0
    for digit in num_str:
        if not digit.isdigit():
            return None
        num = num * 10 + int(digit)
    return num


def conv_float(num_str):
    whole_part, decimal_part = num_str.split('.')
    if not whole_part.isdigit() or not decimal_part.isdigit():
        return None
    return float(f"{whole_part}.{decimal_part}")


def conv_hex(num_str):
    num = 0
    for digit in num_str:
        if not digit.isdigit() and not ('a' <= digit <= 'f'):
            return None
        num = num * 16 + (int(digit) if digit.isdigit() else ord(digit) - ord('a') + 10)
    return num
