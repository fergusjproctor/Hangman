def heading(word, number=1):
    level = '#'
    if number > 6:
        return f'{6*level} {word}'
    if number < 1:
        return f'{level} {word}'
    return f'{number*level} {word}'
