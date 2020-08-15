# EX1--This will utilize Try/Except to handle a divide by zero error
def div42by(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')


print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))
# output ==
# 21.0
# 3.5
# Error: You tried to divide by zero.
# None
# 42.0


# EX2--This will utilize Try/Except to validate the input is an integer/avoid a ValueError
print('How many dogs do you have?')
numDogs = input()
try:
    if int(numDogs) >= 4:
        print('That is a lot of dogs!')
    elif int(numDogs) < 0:
        print('That is not possible!')
    else:
        print('That is an acceptable number of dogs.')
except ValueError:
    print('Please enter an integer value.')
# output ==
# How many dogs do you have?
# -5
# That is not possible!

# output ==
# How many dogs do you have?
# 7
# That is a lot of dogs!

# output ==
# How many dogs do you have?
# fifteen
# Please enter an integer value.




