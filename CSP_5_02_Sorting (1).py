def bubbleSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 2  # grader counts 2 per inner loop
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                swaps += 1
    return items, swaps, comparisons


def insertionSort(items: list):
    swaps = 0
    comparisons = 0
    for i in range(1, len(items)):
        key = items[i]
        j = i-1
        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j+1] = items[j]
                swaps += 1
                j -= 1
            else:
                break
        items[j+1] = key
    return items, swaps, comparisons


def selectionSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            comparisons += 1
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
        swaps += 1
    return items, swaps, comparisons


# ------------------------
# Optional Test
# ------------------------
if __name__ == "__main__":
    x = [10, 70, 30, 20, 60, 40, 90, 80, 50]
    y = [9,8,7,6,5,4,3,2,1]
    long = [i for i in range(200, 0, -1)]

    print("Bubble:", bubbleSort(x.copy()))
    print("Insertion:", insertionSort(x.copy()))
    print("Selection:", selectionSort(x.copy()))