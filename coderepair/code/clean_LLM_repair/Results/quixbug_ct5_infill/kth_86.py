def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)else:kth(above, k)

    elsek)
Quietkk)
Quiet elifk )
Quiet elif k >=return kth(below, k)
Quiet elif kkth(arr, k)
Quiet else:
Datetime#return= [.]
    else:
        return pivot