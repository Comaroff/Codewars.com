def array_diff(a, b):
    for i in range(len(a)):
        for j in b:
            if j in a:
                a.remove(j)
            else:
                pass
    return a

print(array_diff([1, 2, 2, 2, 3, 4, 2, 7], [3, 2, 7]))
