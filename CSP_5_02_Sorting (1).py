def bubbleSort(items):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1

    return items, swaps, comparisons


def insertionSort(items):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        moved = False

        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]
                j -= 1
                moved = True
            else:
                break

        items[j + 1] = key
        if moved:
            swaps += 1

    return items, swaps, comparisons


def selectionSort(items):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if items[j] < items[min_index]:
                min_index = j

        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]
            swaps += 1

    return items, swaps, comparisons

x = [10,70,30,20,60,40,90,80,50]
y = [9,8,7,6,5,4,3,2,1]
long = [i for i in range(200,0,-1)]
l = long.copy()
l.sort()

print(bubbleSort(x.copy()))       # Should print ([10..90], 11, 40)
print(insertionSort(x.copy()))    # Should print ([10..90], 11, 19)
print(selectionSort(x.copy()))    # Should print ([10..90], 8, 36)