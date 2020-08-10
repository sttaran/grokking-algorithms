def quick_sort(arr):
    if(len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        less = [value for value in arr[1:] if value <= pivot]
        greater = [value for value in arr[1:]if value > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


myArr = [1, 213, 3, 5, 2, 23, 45, 75, 32, 65, 34, 21, 8, 7]
print(quick_sort(myArr))
