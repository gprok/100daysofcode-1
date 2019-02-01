def permute(s, start, end, plist):
    if start == end:
        ps = ''.join(s)
        if ps not in plist:
            plist.append(ps)
    else:
        for i in range(start,end+1):
            s[start], s[i] = s[i], s[start]
            permute(s, start+1, end, plist)
            s[start], s[i] = s[i], s[start] # backtrack

def permutations(string):
    plist = []
    s = list(string)
    permute(s, 0, len(string)-1, plist)
    return plist


print(sorted(permutations('a'))) # ['a']
print(sorted(permutations('ab'))) # ['ab', 'ba']
print(sorted(permutations('aabb'))) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
