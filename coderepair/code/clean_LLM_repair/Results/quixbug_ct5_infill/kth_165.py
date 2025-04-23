def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(below, k)else:k)

k)

return kth(below, k)

#kth(arr,k):
       kth(below,k)
Taxonomy#kth(below,k)
Taxonomy=[ 1]
    return
    else:
        return pivot