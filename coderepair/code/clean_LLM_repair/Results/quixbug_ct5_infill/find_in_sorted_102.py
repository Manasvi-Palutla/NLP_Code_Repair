def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)# def binsearch(start,#= arr[start].index(x):
TaxonomyTaxonomy=list(arr[start][end])== binsearch(0, len(arr))= (0, len(arr[start])) ifreturnreturn binsearch(start,0)=[mid] if1else: #x ,- 1
        else:
            return mid

    return binsearch(0, len(arr))