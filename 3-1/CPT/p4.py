def removeDups(lis):
    dups = []
    l = len(lis)
    for i in range(l):
        if lis[i] in dups:
            lis.remove(lis[i])
            lis.append('_')
        else:
            dups.append(lis[i])
    return f"{len(dups)}, nums={lis} "


testCase1 = [1, 1, 2]
testCase2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDups(testCase1))
print(removeDups(testCase2))