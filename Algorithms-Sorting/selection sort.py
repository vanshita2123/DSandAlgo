# rarely used as time complexity and space complexity is too high

def selection_sort(arr):
     i = 0
     while i < len(arr):
         min = a[i]
         index = i
         for j in range(i+1, len(arr)):
             if a[j] < min:
                 min = a[j]
                 index = j
         arr[i], arr[index] = arr[index], arr[i]
         i+=1
     return arr

a = [32, 84, 30, 21, 4, 90, 65, 47, 1, 36, 77]
print(selection_sort(a))

