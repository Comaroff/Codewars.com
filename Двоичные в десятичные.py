def binary_array_to_number(arr):
    arr.reverse()
    b = 0
    s = 0
    for i in range(len(arr)):
        s += arr[i] * (2 ** b)
        b += 1
    return s

print(binary_array_to_number([1, 0, 0, 1]))