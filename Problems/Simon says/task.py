def what_to_do(instructions):
    word = 'Simon says'
    if word in instructions:
        instructions = instructions.replace(word, '')
        return 'I {}'.format(instructions)
    else:
        return "I won't do it!"



