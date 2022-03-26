def in_array(array1, array2):
    r = []
    for i in array1:
        for j in array2:
            if i in j:
                r.append(i)
    if len(r) > 0:
        b = list(set(r))
        b.sort()
        return b
    else:
        return []




a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))