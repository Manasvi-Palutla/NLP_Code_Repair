def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(below, k)return kth(below, k)
   return kth(above, k)k>= num_less:
       else:
AccessToken =)return pivot #Ktharr,k+ 1] #return#returnarr[1] #ifreturn#else:
AccessToken return##if#if#if
    else:
        return pivot