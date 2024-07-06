romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romanToInt(r):
    l = len(r)
    n = 0
    for i in range(l):
        if i < l - 1 and romans[r[i]] < romans[r[i+1]]:
            n -= romans[r[i]]
        else:
            n += romans[r[i]]
    return n


print(romanToInt('MCMXCIV'))
