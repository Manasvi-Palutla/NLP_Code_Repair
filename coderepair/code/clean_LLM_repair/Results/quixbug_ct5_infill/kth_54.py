def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)=0return kth(below,k)
   ]

   : if num_lessoreq >:kth(below, k)
   else:
       -k)
   k )
   if== 1:
       
    else:
        return pivot