def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(below, k)return kth(below,=)[ 0 ]]= arr[1]len(above): return pivot #(arr[0],) return[ 1k in) ,( )
    else:
        return pivot