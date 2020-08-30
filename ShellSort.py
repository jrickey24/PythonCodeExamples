numbers = [31, 15, 7, 3, 1]


def insertion_sort_interleaved(numbers, start_index, gap):
    for i in range(start_index + gap, len(numbers), gap):
        j = i
        while (j - gap >= start_index) and (numbers[j] < numbers[j - gap]):
            temp = numbers[j]
            numbers[j] = numbers[j - gap]
            numbers[j - gap] = temp
            j = j - gap


def shell_sort(numbers, gap_values):
    for gap_value in gap_values:
        for i in range(gap_value):
            insertion_sort_interleaved(numbers, i, gap_value)


print('Original List: ' + str(numbers[0:]))


print('Insertion Sort Interleaved List: ' + str(insertion_sort_interleaved(numbers[0:1])))
