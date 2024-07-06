testCase1 = " Hello World "
testCase2 = " fly me to the moon "
testCase3 = " luffy is still joyboy "


def lastWordLen(s):
    s.strip()
    l = s.split()
    return len(l[-1])


print(lastWordLen(testCase1))
