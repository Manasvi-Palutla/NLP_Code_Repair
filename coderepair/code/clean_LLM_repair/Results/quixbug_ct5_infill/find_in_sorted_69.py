def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(mid+1, end)for0#[=for i in range(len(arr))= arr[i]= arr[i]= arr[i-1] return] =] if!=[]
        else:
            return mid

    return binsearch(0, len(arr))