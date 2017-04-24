def negabase(i,b,alphabet):
    digits = []
    if not i:
        digits = [alphabet[0]]
    else:
        while i != 0:
            i, remainder = divmod(i, b)
            if remainder < 0:
                i, remainder = i + 1, remainder + abs(b)
            digits.append(str(alphabet[remainder]))
    return ''.join(digits[::-1])

def negabasetodec(digits,alphabet,base,offset=0):
    r = 0
    for n in digits:
        r = r*base + (alphabet.index(n) - offset)
    return r


xerossubase = "ONMLKJIHGFEDCBA0abcdefghijklmno"
