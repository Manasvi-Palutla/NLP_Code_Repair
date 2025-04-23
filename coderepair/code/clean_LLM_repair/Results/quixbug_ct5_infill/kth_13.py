def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        
        return kth(below, k)returnk)
   elif k > num_less:
returnk)
SearchResult elif k >=k):
        return kth(above, k)
SearchResultreturnreturn kth(arr,k)
   = len(arr)k:

else:
 nodeID]= ( 1#k)

    else:
        return pivot