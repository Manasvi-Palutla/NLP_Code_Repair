def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid+1, end)return -1for= 1[ 0 ]=== arr[mid-1]:
            == arr[mid]=+mid_key ,]]]( ( arr [ mid_key=:[[ mid_key ] =][ mid ]=.] ,else : if (
        else:
            return mid

    return binsearch(0, len(arr))