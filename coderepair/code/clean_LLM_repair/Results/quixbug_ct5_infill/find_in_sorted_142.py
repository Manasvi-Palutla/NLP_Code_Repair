def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid) def find_in_sorted_seq_iterator (()forlen(arr):=" + " ] if== "0" else== "0""0" else"1" return"0" else :"0" ,,return[ "1" ,, "2", "2" , "3"
        else:
            return mid

    return binsearch(0, len(arr))