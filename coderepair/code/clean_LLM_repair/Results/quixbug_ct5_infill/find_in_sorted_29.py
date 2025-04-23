def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start, mid+1)returnreturn binsearch(0,1)
KeyspaceIDif len(arr) >: if x >) return mid_seq_order_idx:xxelse :for ix < arr[i]:fori in range(i):returnx )
        else:
            return mid

    return binsearch(0, len(arr))