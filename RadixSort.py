# Returns the maximum length, in number of digits, out of all list elements
def radix_get_max_length(my_numbers):
    max_digits = 0
    for num in my_numbers:
        digit_count = radix_get_length(num)
        if digit_count > max_digits:
            max_digits = digit_count
    return max_digits


# Returns the length, in number of digits, of value
def radix_get_length(value):
    if value == 0:
        return 1

    digits = 0
    while value != 0:
        digits += 1
        value = value // 10
    return digits


def radix_sort(my_numbers):
    buckets = []
    for i in range(10):
        buckets.append([])

    # Find the max length, in number of digits
    max_digits = radix_get_max_length(my_numbers)

    pow_10 = 1
    for digit_index in range(max_digits):
        for num in my_numbers:
            bucket_index = (num // pow_10) % 10
            buckets[bucket_index].append(num)

        my_numbers.clear()
        for bucket in buckets:
            my_numbers.extend(bucket)
            bucket.clear()

        pow_10 = pow_10 * 10

    negatives = []
    non_negatives = []
    for num in my_numbers:
        if num < 0:
            negatives.append(num)
        else:
            non_negatives.append(num)
    negatives.reverse()
    my_numbers.clear()
    my_numbers.extend(negatives + non_negatives)


# Create a list of unsorted values
my_numbers = [47, 81, 13, 5, 38, 96, 51, 64]

# Print unsorted list
print('UNSORTED:', my_numbers)

# Call radix_sort to sort the list
radix_sort(my_numbers)

# Print sorted list
print('SORTED:', my_numbers)
