def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        
        return kth(above, k)return=k - num_less:
returnk-num_lessoreq-1= k-num_lessoreq:0#k#k>=num_lessoreq, k =#k-num_lessoreqkth(below,num_less:
k-1)
AccessToken
    else:
        return pivot