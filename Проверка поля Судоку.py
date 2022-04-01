def valid_solution(a):
    import numpy as np
    pole = np.array(a)
    gen = []
    k = 3
    f = 3
    if np.count_nonzero(pole) == 81:
         pass
    else:
         return False
    for i in range(len(pole)):
        if np.count_nonzero(np.unique(pole[:, i])) != 9:
            return False
        else:
            gen.append(1)
    for j in range(len(pole)):
        if np.count_nonzero(np.unique(pole[j, :])) != 9:
            return False
        else:
            gen.append(1)
    for j in range(len(pole)):
        for i in range(len(pole[j])):
            while f < (len(pole) + 1) and k < (len(pole) + 1):
                if np.sum(pole[i:k, j:f].ravel()) != 45:
                    return False
                else:
                    gen.append(1)
                if len(pole[i:k, j:f].ravel()) != len(np.unique(pole[i:k, j:f])):
                    return False
                else:
                    gen.append(1)
                j += 3
                f += 3
                if f > len(pole):
                    i += 3
                    k += 3
                    j = 0
                    f = 3
    if len(gen) > 0:
        return True
    else:
        return False

print(valid_solution([[5, 3, 4, 6, 7 , 8, 9, 1, 2],
                       [6, 7, 2, 1, 9, 5, 3, 4, 8],
                       [1, 9, 8, 3, 4, 2, 5, 6, 7],
                       [8, 5, 9, 7, 6, 1, 4, 2, 3],
                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
                       [9, 6, 1, 5, 3, 7, 2, 8, 4],
                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
                       [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                       [6, 7, 2, 1, 9, 0, 3, 4, 9],
                       [1, 0, 0, 3, 4, 2, 5, 6, 0],
                       [8, 5, 9, 7, 6, 1, 0, 2, 0],
                       [4, 2, 6, 8, 5, 3, 7, 9, 1],
                       [7, 1, 3, 9, 2, 4, 8, 5, 6],
                       [9, 0, 1, 5, 3, 7, 2, 1, 4],
                       [2, 8, 7, 4, 1, 9, 6, 3, 5],
                       [3, 0, 0, 4, 8, 1, 1, 7, 9]]))

print(valid_solution([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]))


print(valid_solution([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [2, 3, 4, 5, 6, 7, 8, 9, 1],
                    [3, 4, 5, 6, 7, 8, 9, 1, 2],
                    [4, 5, 6, 7, 8, 9, 1, 2, 3],
                    [5, 6, 7, 8, 9, 1, 2, 3, 4],
                    [6, 7, 8, 9, 1, 2, 3, 4, 5],
                    [7, 8, 9, 1, 2, 3, 4, 5, 6],
                    [8, 9, 1, 2, 3, 4, 5, 6, 7],
                    [9, 1, 2, 3, 4, 5, 6, 7, 8]]))