def quicksort(array, left, right):
    length = len(array)
    if left < right:
        pivot = right
        partitionindex = partition(array, pivot, left, right)

        quicksort(array, left, partitionindex-1)
        quicksort(array, partitionindex+1, right)
    return array

def partition(array, pivot, left, right):
    pivotvalue = array[pivot]
    partitionindex = left

    for i in range(left, right):
        if array[i] < pivotvalue:
            swap(array, i, partitionindex)
            partitionindex += 1

    swap(array, right, partitionindex)
    return partitionindex

def swap(array, firstindex, secondindex):
    temp = array[firstindex]
    array[firstindex] = array[secondindex]
    array[secondindex] = temp


numbers = [48, 21, 30, 5, 99, 60, 36, 12, 78, 56]
print(quicksort(numbers, 0, len(numbers)-1))
