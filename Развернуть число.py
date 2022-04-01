def expanded_form(num):
    copy = str(num)
    j = 1
    itog = []
    summach = []
    for i in copy[::-1]:
        itog.append(int(i) * j)
        j *= 10
    finish = sorted(itog, reverse=True)
    for i in finish:
        if i != 0:
            summach.append(i)

    s = ' + '.join(map(str, summach))

    return s



expanded_form(12)  # Should return '10 + 2'
expanded_form(42)  # Should return '40 + 2'
expanded_form(743)
print(expanded_form(70304))# Should return '70000 + 300 + 4'