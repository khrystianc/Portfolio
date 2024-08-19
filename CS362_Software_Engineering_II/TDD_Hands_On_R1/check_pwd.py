def check_pwd(pwd):

    # Check password length
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    
    # Check for an uppercase letter
    has_uppercase = False
    for i in pwd:
        if i.isupper():
            has_uppercase = True
            break
    if not has_uppercase:
        return False
    
    # Check for a lowercase letter
    has_lowercase = False
    for i in pwd:
        if i.islower():
            has_lowercase = True
            break
    if not has_lowercase:
        return False
    
    # Check for a digit
    has_digit = False
    for i in pwd:
        if i.isdigit():
            has_digit = True
            break
    if not has_digit:
        return False

    # Check for a symbol
    the_symbols = '~`!@#$%^&*()_+-='
    has_symbol = False
    for i in pwd:
        if i in the_symbols:
            has_symbol = True
            break
    if not has_symbol:
        return False
    
    return True