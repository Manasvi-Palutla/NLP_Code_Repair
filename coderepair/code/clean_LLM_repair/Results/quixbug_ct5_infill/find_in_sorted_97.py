def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)for x in==1 ,,== 1= 1= 0 return#if= x.find('='): #is not None: #: #if#else: #x.find('=') #ifx.find('='):#-1 #endif#endif= 1 for iii:
        else:
            return mid

    return binsearch(0, len(arr))