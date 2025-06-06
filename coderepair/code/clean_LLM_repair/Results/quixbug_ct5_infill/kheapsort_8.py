def kheapsort(arr, k):

    heap = arr[:k]
    heapq.heapify(heap)

    x = arr[:k]
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)