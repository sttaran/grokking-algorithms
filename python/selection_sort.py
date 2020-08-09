def get_smallest(arr):
    smallest = arr[0]
    index_of_smallest = 0
    for idx in range(1, len(arr)):
        if (arr[idx] < smallest):
            smallest = arr[idx]
            index_of_smallest = idx
    return index_of_smallest


def selectionSort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = get_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


print(selectionSort([2, 5, 6, 7, 10, 11, 14, 54, 37, 89, 4, 1]))
