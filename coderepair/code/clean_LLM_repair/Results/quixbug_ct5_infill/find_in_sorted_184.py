def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid)= len(arr):] = x## return[] if len== 2:
            = len(arr[0])1= len(arr[0]) return (
        else:
            return mid

    return binsearch(0, len(arr))