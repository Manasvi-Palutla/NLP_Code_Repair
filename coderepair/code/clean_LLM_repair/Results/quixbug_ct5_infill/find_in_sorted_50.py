def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start == end:
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)
        elif x > arr[mid]:
            return binsearch(end, mid)mid(forin arr#print("Findfound in sortedx):print("Finding in sorted(arr, x) print("foundx) print "Finding in sorted
        else:
            return mid

    return binsearch(0, len(arr))