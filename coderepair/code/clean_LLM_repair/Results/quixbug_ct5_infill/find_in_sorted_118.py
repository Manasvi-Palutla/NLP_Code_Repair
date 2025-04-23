def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(start, mid+1)== arr= arr[mid][1]=# 2
+ 1seq1= # 2seq1 =#2seq1= #2seq1= #2seq1#= #2 #3#, #3#3##7seq1#3seq2#1seq2#4,#4
        else:
            return mid

    return binsearch(0, len(arr))