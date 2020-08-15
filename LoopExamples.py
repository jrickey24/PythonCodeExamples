# while loop
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))
# output ==
# spam is 1
# spam is 2
# spam is 4
# spam is 5


# for loop
print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))
# output ==
# My name is
# Jimmy Five Times 0
# Jimmy Five Times 1
# Jimmy Five Times 2
# Jimmy Five Times 3
# Jimmy Five Times 4