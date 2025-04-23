def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)seqid
CTYPE= arr[mid]:seqid =# if len(seqid):seqid=)seqid== mid:seqid1:seqid + 1returnreturn mid_id= [1]
        else:
            return mid

    return binsearch(0, len(arr))