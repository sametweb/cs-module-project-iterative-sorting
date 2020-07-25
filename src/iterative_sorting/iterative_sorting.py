# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr


print('Selection Sort', selection_sort([7, 9, 4, 7, 6, 3, 6, 1, 0, 9, 5]))
# Selection Sort [0, 1, 3, 4, 5, 6, 6, 7, 7, 9, 9]


# TO-DO:  implement the Bubble Sort function below

def bubble_sort(arr):
    # Your code here
    swapped = 1

    while swapped > 0:
        swapped = 0
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped += 1

    return arr


print('Bubble Sort', bubble_sort([7, 9, 4, 7, 6, 3, 6, 1, 0, 9, 5]))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the
buckets.

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    if maximum is None:
        maximum = 0
        for num in arr:  # O(n)
            if num > maximum:
                maximum = num

    my_list = [0 for i in range(maximum + 1)]  # O(n)

    for i in arr:  # O(n)
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"

        my_list[i] += 1

    arr = []  # After this point, I don't need the original array

    for i, num in enumerate(my_list):
        for j in range(num):
            arr.append(i)

    return arr


print('Counting Sort', counting_sort([7, 9, 4, 7, 6, 3, 6, 1, 0, 9, 5]))
