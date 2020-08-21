def check_email(string):
    return '@' in string and '.' in string[string.find('@') + 2:] and ' ' not in string

