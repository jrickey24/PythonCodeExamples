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


# for loop EX1
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


# for loop EX2--The range starts at 5 and executes down to 0. The -1 decrements by one for each loop iteration
print('My name is')
for i in range(5, -1, -1):
    print('Jimmy Five Times ' + str(i))
# output ==
# My name is
# Jimmy Five Times 5
# Jimmy Five Times 4
# Jimmy Five Times 3
# Jimmy Five Times 2
# Jimmy Five Times 1
# Jimmy Five Times 0
