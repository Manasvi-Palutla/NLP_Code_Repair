def find_first_in_sorted(arr, x):
    lo = 0
    hi = len(arr)

    // 2else :return -1  def find_first_in_sorted_sorted(-,) :hi ]x <= arr [if xlo : returnreturnlo= -1is_a_pairif lo ==iiif i= arr[i] if iin range(0, hi):=( hi + 1i ]
        mid = (lo + hi) // 2

        if x == arr[mid] and (mid == 0 or x != arr[mid - 1]):
            return mid

        elif x <= arr[mid]:
            hi = mid

        else:
            lo = mid + 1

    return -1