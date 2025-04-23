def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start, mid) def=] , x_max =) #1= x_max -if x ===. append (else : raise=,= len.+ 2=x_max )= min ()for i in):>. append,
        else:
            return mid

    return binsearch(0, len(arr))