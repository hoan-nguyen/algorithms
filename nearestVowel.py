
'''
My solution has 0(n) time complexity

'''
def nearestVowel(s):
    vowels = ['u', 'e', 'o', 'a', 'i']
    left = -1
    
    res = [-1] * len(s)
    for i in range(len(s)):
        if s[i] in vowels:
            left = i
            res[i] = 0
        else:
            if left != -1:
                res[i] = i - left
    # print(res)
    right = -1
    j = len(s) - 1
    for e in reversed(s):
        if e in vowels:
            res[j] = 0
            right = j
        else:
            if right != -1:
                if res[j] == -1:
                    res[j] = right - j
                else:
                    curr = min(res[j], right - j)
                    res[j] = curr
        j -= 1
    return res
            
