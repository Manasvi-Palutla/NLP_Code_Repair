def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(below, k)else: return= arr[k]
Apps =inin range(len(below)>=elsekth(above, k)
Apps#print("kth",kth(below, k))
Appskh(below, k)
Apps
    else:
        return pivot