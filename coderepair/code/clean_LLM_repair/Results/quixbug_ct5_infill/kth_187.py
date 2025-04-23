def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)returnk)
   if k ==k:
        returnk)
   return kth(arr, k)

#len(k) if num_lessoreq:
        =num_lessoreq#len(k)k in#k ==k >=K(k)/len(k)#
    else:
        return pivot