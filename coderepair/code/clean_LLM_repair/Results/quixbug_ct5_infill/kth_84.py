def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        
        return kth(above, k)elsereturnelse:
       k)
    else:
       =) for x in]x if x > pivotx(]. append (if x <= pivot :)= 0(return kth(arr, k) else
    else:
        return pivot