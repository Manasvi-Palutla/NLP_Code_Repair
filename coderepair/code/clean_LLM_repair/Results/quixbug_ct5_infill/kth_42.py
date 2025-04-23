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
   else:
        returnk)
   len(arr)len(arr): # Kth(arr, k)# #) else :# if k <k<= num_less: #k <#kth(arr, k)
   # else: ## else:#. append (k
    else:
        return pivot