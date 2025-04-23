def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid-1)x , arr)return arr[mid][1]arr[mid][1]]: return binsearch(0,] if x < arr[mid]:if==if: return x:[ mid] [0]1] if x <return] [ 1 ]
        else:
            return mid

    return binsearch(0, len(arr))