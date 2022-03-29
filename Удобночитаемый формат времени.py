def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        hour = seconds // 3600
        hourfin = hour % 24
        day = hour // 24
        dayfin = day % 365
        year = day // 365

        minsec = seconds % 3600
        minuta = minsec // 60
        sec = minsec % 60
        god = {'year': year, 'day': dayfin, 'hour': hourfin, 'minute': minuta, 'second': sec}

        god = {k: v for k, v in god.items() if v != 0}

        itog = []
        for k, v in god.items():
            if 1 < v:
                k += 's'
            itog.append(v)
            itog.append(k)
        x = itog[-2:]
        del itog[-2:]
        perv = ''
        for i, item in enumerate(itog[::]):
            if i % 2 != 0:
                perv += str(item) + ', '
            else:
                perv += str(item) + ' '

        res_perv = perv[:-2] + ' '

        convertItog = ' '.join(map(str, x))

        if len(res_perv) > 2:
            res_perv += 'and '
            return res_perv + convertItog
        else:
            return convertItog


print(format_duration(61))
print(format_duration(3153639888776))