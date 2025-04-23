def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)else:=forinlen(arr): if x>=kth(below, k)
AccessToken returnelse:
AccessToken returnkth(arr,k)
AccessToken elifreturnk=len(arr)else:
AccessTokenk
    else:
        return pivot