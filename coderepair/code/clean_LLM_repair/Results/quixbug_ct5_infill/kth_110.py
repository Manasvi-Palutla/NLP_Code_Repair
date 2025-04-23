def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(below, k)k)

   = arr[k+1]
SearchResultreturn kth(below, k)
SearchResult:for xin sorted(arr): #print(x)k==0:print(x)#returnreturn kth(below, k) return
    else:
        return pivot