def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)fori in range(len(arr))=for i[ i ]]== 1= 1is_key:1<= mid:= 0: returnmax (:) ,== 2return 1= 10 )2 ]0 ]] :) )
        else:
            return mid

    return binsearch(0, len(arr))