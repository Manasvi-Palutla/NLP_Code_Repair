def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)kk)
   k)

k )kth(above, k)
    else:
= k < num_lessoreq:else:
kk<=num_lessoreq:
       kth(below, k)
   else:
        return kth(below, k)
   
    else:
        return pivot