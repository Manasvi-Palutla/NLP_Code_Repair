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
kth(above, k)
   #kth(arr, k)

ifkth(below, k)
SearchResultelse:return pivotelif k == num_lessoreq:
for x in] ]return
    else:
        return pivot