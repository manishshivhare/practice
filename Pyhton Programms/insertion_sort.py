arr = [14, 25, 78, 95, 34, 75, 94, 19, 15, 49]
for i in range(0, len(arr)):
    value = arr[i]
    hole = i
    while (hole != 0 and arr[hole-1] > value):
        arr[hole] = arr[hole - 1]
        hole = hole-1
    arr[hole] = value
print(arr)
