def maskify(cc):
    c = cc[-4:]
    b = ""
    for i in cc[0:-4]:
        b += "#"
    return b + c

cc = '885178511587966'
r = maskify(cc)
print(r)
