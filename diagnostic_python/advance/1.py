def alphabet_reverse(string):
    def choose_max(s, smax):
        if len(s) > len(smax):
            smax = s
        elif len(s) == len(smax) and len(s) > 0:
            if ord(s[0]) < ord(smax[0]):
                smax = s
        s = ''
        return s, smax
    smax = s = ''
    for i in range(len(string)-1):
        word1 = string[i]
        ord1 = ord(word1)
        word2 = string[i+1]
        ord2 = ord(word2)
        if ord1 > ord2 and i < len(string)-2:
            s += word1
        elif ord1 > ord2 and i == len(string)-2:
            s += word1 + word2
            s, smax = choose_max(s, smax)
        else:
            s += word1
            s, smax = choose_max(s, smax)
    return smax
strings = [
    'JLKEDXJONHCJQLSP', 
    'IRJMQHSFPBEHPKI',
    'QCOZJ',
    'COXDEAWPFIICB',
    'TLXSDAQMJRNR'
]
for string in strings:
    print(alphabet_reverse(string))
