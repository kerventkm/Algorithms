# this is insert the last element of array into previous sorted array, O(n)
def insertionSort1(n, arr):
    k = arr[-1]
    if k < arr[0]:
        new_wrrr = [k]
        new_wrrr.extend(arr[:(n-1)])
    for i in reversed(range(n-1)):
        if arr[i] > k:
            arr[i+1] = arr[i]
            print(*arr, sep=' ')
        else:
            arr[i+1] = k
            print(*arr, sep=' ')
            break
    if k < arr[0]:
        print(*new_wrrr, sep=' ')
        
arr = [2, 3, 5, 6, 7, 8, 9, 10, 4]
n = 9

insertionSort1(n, arr)