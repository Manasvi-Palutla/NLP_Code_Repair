def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)= arr[1]
AccessToken==1]= arr [- 1]
AccessToken return kth(below,k)
AccessTokenelse :k ==k >= num_less:returnelse:
AccessToken) #k ==k < k :: return)
AccessToken
    else:
        return pivot