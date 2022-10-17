def longestCommonPrefix(strs):
    x = -1
    main = ''
    while x >= -1:
        x += 1
        sub = ''
        for i in strs:
            try:
                sub += i[x]
            except:
                x = -2
        if all(x == sub[0] for x in sub) and len(sub) == len(strs):
            main += sub[0]
        else:
            break
        print(sub)
    if main:
        return main
    else:
        return ''
print(longestCommonPrefix(["cir","car"]))