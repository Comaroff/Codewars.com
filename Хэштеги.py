def generate_hashtag(s):
    if len(s) == 0:
        return False
    else:
        f = s.title()
        f1 = '#' + ''.join(f.split())
        if len(f1) <= 140:
            return f1
        else:
            return False


s = "c i n"
print(generate_hashtag(s))
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false