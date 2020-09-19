# if you're worried about worst case complexity, you should use merge sort but its space complexty is high

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    length = len(arr)
    mid = length//2
    left = arr[:mid]
    right = arr[mid:]
    print('Left {}'.format(left))
    print('Right {}'.format(right))

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    leftindex = 0
    rightindex = 0
    while leftindex < len(left) and rightindex < len(right):
        if left[leftindex] < right[rightindex]:
            result.append(left[leftindex])
            leftindex += 1
        else:
            result.append(right[rightindex])
            rightindex += 1

    print(left, right)
    print(result + left[leftindex:] + right[rightindex:])
    return result + left[leftindex:] + right[rightindex:]

arr = [34, 90, 12, 23, 1, 66, 75, 94, 30, 19]
x = merge_sort(arr)
print("\nFinal array: \n")
print(x)