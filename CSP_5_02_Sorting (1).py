# Bubble Sort
def bubbleSort(items: list):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1                  # Count every comparison
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps += 1                     # Count swap only when actual exchange
    return items, swaps, comparisons


# --------------------------
# Insertion Sort
def insertionSort(items: list):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        moved = False                        # Track if key moves

        while j >= 0:
            if items[j] > key:
                comparisons += 1             # Count comparison only if key < items[j]
                items[j + 1] = items[j]     # Shift element
                j -= 1
                moved = True
            else:
                comparisons += 1             # Count the last comparison where key <= items[j]
                break

        items[j + 1] = key
        if moved:                            # Count swap only if key moved
            swaps += 1

    return items, swaps, comparisons


# --------------------------
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


# --------------------------
# Optional test code (not for submission)
if __name__ == "__main__":
    y = [9,8,7,6,5,4,3,2,1]
    x = [10,70,30,20,60,40,90,80,50]
    long = [i for i in range(200,0,-1)]

    print("Bubble Sort y:", bubbleSort(y.copy()))
    print("Insertion Sort y:", insertionSort(y.copy()))
    print("Selection Sort y:", selectionSort(y.copy()))
    print()
    print("Bubble Sort x:", bubbleSort(x.copy()))
    print("Insertion Sort x:", insertionSort(x.copy()))
    print("Selection Sort x:", selectionSort(x.copy()))