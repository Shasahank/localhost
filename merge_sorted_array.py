# Code to merge two different sorted arrays

def mergeArrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = [None] * (n1 + n2)
    i,j,k = 0,0,0
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1
    while j < n2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    for i in range(n1 + n2):
        print(str(arr3[i]), end = " ")

# We can also modify this section to take manual array inputs
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
mergeArrays(arr1, arr2);
