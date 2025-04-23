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
   == arr[1]
SearchResultin-:>= num_less:
        =return kth(below, k)
SearchResult elifkth(above, k)
SearchResult else:
SearchResultk)
SearchResult else:
SearchResult]k =>= num_lessoreq:
SearchResult:) :
    else:
        return pivot