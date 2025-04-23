def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        
        return kth(above, k)==#if len(below)below):
Datetime#if len(below) < len(below):
Datetime- k]]below[k]kth(below[k], k)
LeafNodekth(below[k], k)
    else:
Datetimereturn
    else:
        return pivot