def beautifulText(s, l, r):
    
    for m in range(l, r + 1):
        ans = []
        tmp = ''
        cnt = 0
        flag = False
        
        for i in range(len(s)):
            if flag:
                flag = False
                continue
                
            tmp += s[i]
            cnt += 1
            if cnt == m:
                if i == len(s) - 1:
                    ans.append(tmp)
                    break
                else:
                    if s[i + 1] == ' ':
                        ans.append(tmp)
                        flag = True
                        tmp = ''
                        cnt = 0
                        continue
                    else:
                        ans = []
                        break
                        
        # print('ans = ', ans)
        if isValid(ans):
            return True
    return False
    
def isValid(arr):
    if len(arr) <= 1:
        return False
    temp = len(arr[0])
    for i in range(1, len(arr)):
        if len(arr[i]) != temp:
            return False
    return True
    
