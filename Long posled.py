
def longest_consec(spis, k):
    if len(spis) == 0 or k > len(spis) or k <= 0:
        return ''
    else:
        j = 0
        finish = []
        spisI = spis.copy()
        spisI.sort(reverse=True, key=len)
        s = spisI[0]
        for i in range(len(spis)):
            x = slice(j, k + j, None)
            finish.append(''.join(spis[x]))
            j += 1

        finish.sort(reverse=True, key=len)

        return finish[0]








spis5 =[]
spis4 = ["zone", "abigail", "theta", "form", "libe", "zas"]
spis3 = ["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
spis2 = ["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
spis = ["4444", "555556", "7777777", "666666", "333", "7777777", "6666ss", "ssssss"]

print(longest_consec(spis, 2))
print(longest_consec(spis2, 3))
print(longest_consec(spis3, 1))
print(longest_consec(spis4, 2))
print(longest_consec(spis5, 3))