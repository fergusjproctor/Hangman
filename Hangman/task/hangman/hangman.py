import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
decision = input('Type "play" to play, "exit" to quit: ')
while decision == 'play':
    target_word = random.choice(words)
    hint = '-' * (len(target_word))
    lives = 8
    lettersTried = set()
    while lives > 0 and hint != target_word:
        print('\n' + hint)
        input_letter = str(input('Input a letter: '))
        if len(input_letter) != 1:
            print('You should input a single letter')
            continue
        elif not (input_letter.isascii() and input_letter.islower()):
            print('It is not an ASCII lowercase letter')
            continue
        elif input_letter in lettersTried:
            print('You already typed this letter')
            continue
        else:
            lettersTried.add(input_letter)
        if input_letter not in target_word:
            print('No such letter in the word')
            lives -= 1
        elif input_letter in target_word:
            for j in range(len(target_word)):
                if target_word[j] == input_letter:
                    hint = hint[:j] + target_word[j] + hint[j+1:]
                if hint == target_word:
                    print('You guessed the word {}!'.format(target_word))
                    print('You survived!')
                    break
    else:
        if lives < 1:
            print('You are hanged!')
    decision = input('\nType "play" to play, "exit" to quit: ')
