# Bubble Sort
def bubbleSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1               # Count every comparison
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]  # Swap only when needed
                swaps += 1

    return items, swaps, comparisons


# Insertion Sort
def insertionSort(items: list):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        first_check = True                 # Track first comparison

        while j >= 0:
            comparisons += 1               # Only count actual comparisons
            if items[j] > key:
                items[j + 1] = items[j]   # Shift element
                j -= 1
                first_check = False
            else:
                break

        items[j + 1] = key
        if not first_check:                # Count swap only if key moved
            swaps += 1

    return items, swaps, comparisons


# Selection Sort
def selectionSort(items: list):
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


# ----------------------------
# Example testing
y = [9,8,7,6,5,4,3,2,1]
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("Bubble Sort y:", bubbleSort(y.copy()))
print("Insertion Sort y:", insertionSort(y.copy()))
print("Selection Sort y:", selectionSort(y.copy()))
print()
print("Bubble Sort x:", bubbleSort(x.copy()))
print("Insertion Sort x:", insertionSort(x.copy()))
print("Selection Sort x:", selectionSort(x.copy()))