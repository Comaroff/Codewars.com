def make_readable(seconds):

    hour = seconds // 3600
    minsec = seconds % 3600
    minuta = minsec // 60
    sec = minsec % 60

    return "%02d:%02d:%02d" % (hour, minuta, sec)


print(make_readable(0), "00:00:00")
print(make_readable(5), "00:00:05")
print(make_readable(60), "00:01:00")
print(make_readable(86399), "23:59:59")
print(make_readable(359999), "99:59:59")