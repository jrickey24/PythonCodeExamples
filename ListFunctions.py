# LIST FUNCTIONS
pool_toys = ['Noodle', 'Diving Sticks', 'Goggles', 'Snorkel', 'Goggles', 'Kickboard']

# CREATE A COPY OF THE POOL TOYS LIST & ASSIGN TO EXISTING POOL TOYS LIST
existing_pool_toys = pool_toys.copy()
print('Copying Original Pool Toys List to Existing Pool Toys List...Original Pool Toys List:' + str(pool_toys))
print('Existing Pool Toys List: ' + str(existing_pool_toys))

# REMOVE THE FIRST ITEM INSTANCE FROM THE EXISTING POOL TOYS LIST
# NOTE THAT THE ORIGINAL POOL TOYS LIST IS UNMODIFIED
try:
    existing_pool_toys.remove('Goggles')
    print('Existing Pool Toys List Contains :' + str(existing_pool_toys))
    print('Original Pool Toys List Contains:' + str(pool_toys))
except ValueError:
    print('No item found to remove.')

# CREATE & POPULATE A NEW LIST USING A SUBSET OF AN EXISTING LIST
favorite_pool_toys = pool_toys[1:4]
# favorite_pool_toys == ['Diving Sticks', 'Goggles', 'Snorkel']

# CONCATENATE TWO LISTS TOGETHER TO CREATE A NEW LIST
pool_supplies = ['Sunscreen', 'Towels', 'Cooler', 'Floaties']
all_pool_items = pool_toys + pool_supplies
# all_pool_items ==
# ['Noodle', 'Diving Sticks', 'Goggles', 'Snorkel', 'Goggles', 'Kickboard', 'Sunscreen', 'Towels', 'Cooler', 'Floaties']

# ALL(LIST) FUNCTION-- RETURNS 'True' IF THE LIST IS EMPTY OR ALL ITEMS IN THE LIST != 0, ELSE RETURNS 'False'
my_numbers = []
print(all(my_numbers))  # output == True
my_numbers = [1, 2, 3]
print(all(my_numbers))  # output == True
my_numbers.append(0)
print(my_numbers)  # output == [1, 2, 3, 0]
print(all(my_numbers))  # output == False

# ANY(LIST) FUNCTION--RETURNS 'True' IF ANY LIST ITEM IS != 0, ELSE RETURNS 'False' IF LIST IS EMPTY OR ALL 0 VALUES
print(any(my_numbers))  # True

# RETURNS THE MAX LIST ITEM
print(max(my_numbers))  # 3

# RETURNS THE MIN LIST ITEM
print(min(my_numbers))  # 0

# RETURNS THE SUM OF THE LIST ITEMS
print(sum(my_numbers))  # 6

# EXECUTE THE POP FUNCTION ON THE EXISTING POOL TOYS LIST
# POPS OFF THE -1 ITEM IN THE LIST IF NO INDEX IS SPECIFIED
print(existing_pool_toys)  # ['Noodle', 'Diving Sticks', 'Snorkel', 'Goggles', 'Kickboard']
existing_pool_toys.pop()
print('Existing Pool Toys List after implementing the pop() function Contains:')
print(existing_pool_toys)  # ['Noodle', 'Diving Sticks', 'Snorkel', 'Goggles']

# POP FUNCTION WITH SPECIFIED INDEX
print(existing_pool_toys)  # ['Noodle', 'Diving Sticks', 'Snorkel', 'Goggles']
existing_pool_toys.pop(2)
print(existing_pool_toys)  # ['Noodle', 'Diving Sticks', 'Goggles']

# LIST INSERT FUNCTION
print(existing_pool_toys)  # ['Noodle', 'Diving Sticks', 'Goggles']
existing_pool_toys.insert(1, 'Kickboard')
print(existing_pool_toys)  # ['Noodle', 'Kickboard', 'Diving Sticks', 'Goggles']

# LIST APPEND FUNCTION--USED WHEN YOU WANT TO ADD AN ITEM TO THE END ON THE LIST
print(existing_pool_toys)  # ['Noodle', 'Kickboard', 'Diving Sticks', 'Goggles']
existing_pool_toys.append('Snorkle')
existing_pool_toys.append('Goggles')
print(existing_pool_toys)  # ['Noodle', 'Kickboard', 'Diving Sticks', 'Goggles', 'Snorkle', 'Goggles']

# LIST COUNT FUNCTION
print(existing_pool_toys.count('Goggles'))  # 2

# LIST CLEAR FUNCTION--CLEAR ALL THE ITEMS OF THE LIST
print(existing_pool_toys)  # ['Noodle', 'Kickboard', 'Diving Sticks', 'Goggles', 'Snorkle', 'Goggles']
existing_pool_toys.clear()
print(existing_pool_toys)  # []



