numberList = []
while True:
    newInt = input()
    if newInt == '.':
        break
    numberList.append(float(newInt))
print(min(numberList))
