def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)returnx)=x ) :.. append (( x , 1.0 )return arr[x]= int( x )- 1 )=+ 1= int(x)
        else:
            return mid

    return binsearch(0, len(arr))