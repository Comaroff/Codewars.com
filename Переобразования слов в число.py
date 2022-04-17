def parse_int(string):
    import re
    digit_mil = 'one million'
    if digit_mil in string:
        return 1000000

    digit_9 = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    digit_19 = {'ten': '0', 'eleven': '1', 'twelve': '2', 'thirteen': '3',
                'fourteen': '4', 'fifteen': '5', 'sixteen': '6', 'seventeen': '7',
                'eighteen': '8', 'nineteen': '9'}

    digit_90 = {'twenty': '2', 'thirty': '3', 'forty': '4', 'fifty': '5', 'sixty': '6',
                'seventy': '7', 'eighty': '8', 'ninety': '9'}

    digit_91 = {'twenty-': '2', 'thirty-': '3', 'forty-': '4', 'fifty-': '5',
                'sixty-': '6', 'seventy-': '7', 'eighty-': '8', 'ninety-': '9'}

    digit_100 = False
    digit_102 = False
    digit_103 = False
    new = [0, 0, 0, 0, 0, 0]
    spis2 = []
    spis3 = []
    spis = re.sub('-', '- ', string)
    spisok = spis.split()
    if 'hundred' in spisok:
        digit_100 = True

    if 'thousand' in spisok:
        j = spisok.index('thousand')
        spis2 += spisok[:j]
        spis3 += spisok[j:]

        if 'hundred' in spis2:
            digit_102 = True
        if 'hundred' in spis3:
            digit_103 = True
        for i in range(len(spis2)):
            for k, v in digit_9.items():
                if k == spis2[i] and new[0] == 0 and digit_102 == True:
                    new[0] = int(v)
                elif k == spis2[i]:
                    new[2] = int(v)

            for k, v in digit_19.items():
                if k == spis2[i]:
                    new[1] = 1
                    new[2] = int(v)

            for k, v in digit_90.items():
                if k == spis2[i]:
                    new[2] = int(v)

            for k, v in digit_91.items():
                if k == spis2[i]:
                    new[1] = int(v)
        for i in range(len(spis3)):
            for k, v in digit_9.items():
                if k == spis3[i] and new[3] == 0 and digit_103 == True:
                    new[3] = int(v)
                elif k == spis3[i]:
                    new[5] = int(v)

            for k, v in digit_19.items():
                if k == spis3[i]:
                    new[4] = 1
                    new[5] = int(v)

            for k, v in digit_90.items():
                if k == spis3[i]:
                    new[4] = int(v)

            for k, v in digit_91.items():
                if k == spis3[i]:
                    new[4] = int(v)
    else:
        for i in range(len(spisok)):
            for k, v in digit_9.items():
                if k == spisok[i] and new[3] == 0 and digit_100 == True:
                    new[3] = int(v)
                elif k == spisok[i]:
                    new[5] = int(v)

            for k, v in digit_19.items():
                if k == spisok[i]:
                    new[4] = 1
                    new[5] = int(v)

            for k, v in digit_90.items():
                if k == spisok[i]:
                    new[4] = int(v)

            for k, v in digit_91.items():
                if k == spisok[i]:
                    new[4] = int(v)

    return int(''.join(map(str, new)))

print(parse_int('one'))
print(parse_int('twenty'))
print(parse_int('twenty-six thousand three hundred fifty-nine'))