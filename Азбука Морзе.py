def morse_cod(code_morze):
    az_morze = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.','Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '!': '−−··−−', '.': '......'
                }
    print(code_morze)
    x = az_morze.copy()
    sos = '...---...'
    if sos in code_morze:
        code_morze = code_morze.replace('...---...', '... --- ...')
    probel = code_morze.replace('   ', '  ')
    print(probel)
    
    probel_none = probel.strip()
    print(probel_none)
    
    probel_spis = probel_none.split(' ')
    print (probel_spis)
    
    spisok_buk = ''
    spisok_buk2 = []
    pust = ''
    
    for i in range(len(probel_spis)):
        if probel_spis[i] == pust:
            spisok_buk += ''
            spisok_buk2.append(probel_spis[i])
        for k, v in x.items():
            if probel_spis[i] == v:
                spisok_buk += k
                spisok_buk2.append(k)

    print(ascii(spisok_buk))
    print(ascii("".join(spisok_buk2)))

    spisok_i = ' '.join(spisok_buk2)
    jude = ""
    c = " "
    for i in range(len(spisok_i)):
        if spisok_i[i] != c:
            jude += spisok_i[i]
        elif spisok_i[i] == c and spisok_i[i + 1] == c:
            jude += spisok_i[i]

    return jude


print(morse_cod('.... . -.--   .--- ..- -.. .'))
print(morse_cod(' . '))
print(morse_cod('...---... −−··−−   .... . .-.. .--. ......'))