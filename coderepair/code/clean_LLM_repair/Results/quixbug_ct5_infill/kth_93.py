def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)else:
        returnk):

k:
        return kth(arr[k:],k)
   k)

   =return kth(above, k)
Taxonomy
    else:
        return pivot