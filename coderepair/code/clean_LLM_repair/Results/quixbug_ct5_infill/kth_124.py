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
LeafNode=len(below)
   if>= num_less:return kth(below,if k>= num_lessoreq:return kth(below, k)
   else:returnreturn kth(below, k)
   
    else:
        return pivot