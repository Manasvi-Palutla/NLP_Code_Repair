def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = len(arr) - len(above)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k)return kth(below, k)
   ifkth(above,len(arr)0]
   [ ]]
SEARCH_KEYWORDS: returnk ][ - 1]
SEARCH_KEYWORDS: return. append)k ]]
    else:
        return pivot