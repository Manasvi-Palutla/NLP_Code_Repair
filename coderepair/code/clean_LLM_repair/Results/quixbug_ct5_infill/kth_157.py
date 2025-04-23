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
       )num_lessoreqk):
        return kth(below,k):
        return kth(above, k)

k==len(below) :k:
       k>= num_less:
Datetime return pivotk)

    else:(below)
TTk-1]
TT elseif
    else:
        return pivot