numberList = []
while True:
    newInt = input()
    if newInt == '.':
        break
    else:
        numberList.append(int(newInt))
print(sum(numberList) / len(numberList))



