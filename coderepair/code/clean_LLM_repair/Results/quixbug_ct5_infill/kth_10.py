def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)k)

#
       )kth(arr, k)

k= 0 #( k >= num_lessoreq):=len(below)
   if k > num_lessoreq: #
k
    else:
        return pivot