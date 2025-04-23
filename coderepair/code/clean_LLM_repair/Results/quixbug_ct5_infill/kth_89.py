def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)return kth(below, k)

   returnkth(below, k)

) : return# FIXME:else : returnk < num_less:num_lessoreq)k)
Auxiliaryfor x in[ 1#ifnum_lessoreq] #if= len(below)#else:
Auxiliary
    else:
        return pivot