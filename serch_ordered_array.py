# time complexity is O(logn)

def serch_ordered(V, arr):
    """Searching V from ordered array arr"""
    init = 0
    end = len(arr) - 1
    while True:
        mid = (init + end)//2
        if arr[mid] == V:
            return mid
        elif arr[mid] > V:
            end = mid - 1
        else:
            init = mid +1
            
            
print(serch_ordered(5, [1,2,3,4,5,6,7,8,9]))