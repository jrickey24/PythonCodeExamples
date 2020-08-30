import operator

# sort() Sorts the list elements in place
fruit_list = ["grape", "banana", "apple", "strawberry", "blueberry"]
print('UNSORTED:', fruit_list)
fruit_list.sort()
print('SORTED:', fruit_list)
fruit_list.sort(reverse=True)  # This optional additional parameter results in descending order
print('REVERSE SORTED:', fruit_list)

# sorted()...Provides a new list that consists of the sorted elements of the originally provided list
num_list = [3, 7, 2, 8, 12, 4, 9, 5]
sorted_num_list = sorted(num_list)
reverse_sorted_num_list = sorted(num_list, reverse=True)
print('UNSORTED:', num_list)
print('SORTED:', sorted_num_list)
print('REVERSE SORTED:', reverse_sorted_num_list)
print()

# Additional key function parameter
file_names = ["Grades.xls", "email.txt", "helper.py", "Test.java"]
case_sensitive = sorted(file_names)
case_insensitive = sorted(file_names, key=str.lower)
print('Normal sort:', case_sensitive)
print('Case insensitive sort:', case_insensitive)


# Custom key functions
def key_is_name(element):
    return element[0]


def key_is_id(element):
    return element[1]


class_list_1 = [("Robert", 135216), ("Amir", 612901), ("Jennifer", 194821), ("Ravi", 631104)]
name_result_1 = sorted(class_list_1, key=key_is_name)
id_result_1 = sorted(class_list_1, key=key_is_id)
print('Sort by name:', name_result_1)
print('Sort by id:', id_result_1)


# Using sorted() with operator.itemgetter()
class_list_2 = [("Robert", 135216), ("Amir", 612901), ("Jennifer", 194821), ("Ravi", 631104)]
name_result_2 = sorted(class_list_2, key=operator.itemgetter(0))
id_result_2 = sorted(class_list_2, key=operator.itemgetter(1))
print('Sort by name:', name_result_2)
print('Sort by id:', id_result_2)
