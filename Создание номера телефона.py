def create_phone_number(n):
    for i in range(len(n)):
        n[i] = str(n[i])
    n.insert(0, "(")
    n.insert(4, ")")
    n.insert(5, "")
    n.insert(9, "-")
    num = ''.join(n)
    num = num[:5] + ' ' + num[5:]
    # print("({}{}{}) {}{}{}-{}{}{}{}".format(*n))
    return num



print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # => returns "(123) 456-7890"