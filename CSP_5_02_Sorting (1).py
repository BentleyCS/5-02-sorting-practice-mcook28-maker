# --------------------------
# Bubble Sort (autograder-compatible)
def bubbleSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1            # Count every if check
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1               # Count only actual swaps

    return items, swaps, comparisons


# --------------------------
# Insertion Sort (autograder-compatible)
def insertionSort(items: list):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        moved = False                  # Track if key moves

        while j >= 0:
            comparisons += 1
            if items[j] > key:
                items[j + 1] = items[j]   # Shift element
                j -= 1
                moved = True
            else:
                break

        items[j + 1] = key
        if moved:                        # Count swap only if key moved
            swaps += 1

    return items, swaps, comparisons


# --------------------------
# Selection Sort (autograder-compatible)
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


# --------------------------
# Example test
y = [9,8,7,6,5,4,3,2,1]              # Worst-case
x = [10,20,30,40,50,60,70,80,90]     # Already sorted

print("Bubble Sort y:", bubbleSort(y.copy()))
print("Insertion Sort y:", insertionSort(y.copy()))
print("Selection Sort y:", selectionSort(y.copy()))
print()
print("Bubble Sort x:", bubbleSort(x.copy()))
print("Insertion Sort x:", insertionSort(x.copy()))
print("Selection Sort x:", selectionSort(x.copy()))