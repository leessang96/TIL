def partitioning(l, r):
    pivot = arr[l]

    i, j = l, r
    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[l], arr[j] = arr[j], arr[l]
    return j


def qsort(l, r):
    if l < r:
        pivot = partitioning(l, r)

        qsort(l, pivot - 1)
        qsort(pivot + 1, r)


arr = list(map(int, input().split()))
qsort(0, len(arr) - 1)
print(arr[500000])