def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)num_lessoreq)

k):
        =](below)

    else:
kth(above)

- num_lessoreq)

[ 0]
ObjectReference else :]]returnk= None return
    else:
        return pivot