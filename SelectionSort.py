def selection_sort(numbers):
    for i in range(len(numbers) - 1):

        # Find index of smallest remaining element
        index_smallest = i
        for j in range(i + 1, len(numbers)):

            if numbers[j] < numbers[index_smallest]:
                index_smallest = j
        # Swap numbers[i] and numbers[index_smallest]
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp


# Create a list of numbers to sort
numbers = [10, 2, 78, 4, 45, 32, 7, 11]

# Display the contents of the list
print('UNSORTED:', numbers)

# Call the selection_sort() function
selection_sort(numbers)

# Display the (sorted) contents of the list
print('SORTED:', numbers)
