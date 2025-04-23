def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid+1, end)returnx ,arr[0][1]:i := 1#index=1 #= arr[0].lower().lower() # i.e.x.lower() #=#0index]]return - 1
        else:
            return mid

    return binsearch(0, len(arr))