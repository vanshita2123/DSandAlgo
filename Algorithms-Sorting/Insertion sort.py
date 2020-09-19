# use when only a few numbers and almost sorted data is given

def insertion_sort(arr):
    length = len(arr)
    i = 1
    end = arr[0]
    while i < length:
        if arr[i] < end:
            x = arr.pop(i)
            for j in range(0,i):
                if x < arr[j]:
                    arr.insert(j, x)
                    break
        end = arr[i]
        i+=1
    return arr

a = [8, 37, 64, 20, 91, 75, 45, 53, 2, 9]
print(insertion_sort(a))