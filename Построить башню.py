def tower_builder(n_floors):
    bash = []
    c = '*'
    j = n_floors
    z = 1
    pust = n_floors - 1
    while 0 != j:
        for i in range(j):
            bash.append((pust * ' ') + c * z + (pust * ' '))
            j -= 1
            z += 2
            pust -= 1

    return bash

n_floors = 2
print(tower_builder(n_floors))