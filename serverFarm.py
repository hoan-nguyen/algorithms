# https://app.codesignal.com/company-challenges/two-sigma/JFbFHYb3CmnKDFaSQ

from operator import itemgetter
def serverFarm(jobs, servers):
    if servers == 0:
        return []
    processors = []
    for i in range(servers):
        processors.append([])
    
    tasks = []
    for i in range(len(jobs)):
        tasks.append([jobs[i], i])
        
    tasks.sort(key=itemgetter(0), reverse=True)
    while len(tasks) > 0:
        currTask = tasks[0]

        # main logic
        index = findMin(processors)
        temp = processors[index]
        temp.append(currTask)
        
        processors[index] = temp
        
        # end main logic
        tasks = tasks[1:]
        tasks.sort(key=itemgetter(0), reverse=True)
    
    print(processors)
    ans = []
    for i in range(len(processors)):
        temp = []
        for j in range(len(processors[i])):
            temp.append(processors[i][j][1])
        ans.append(temp)
    
    return ans
    

def findMin(processors):
    index = 0
    s = sum(helper(processors[0]))
    
    for i in range(1, len(processors)):
        if sum(helper(processors[i])) < s:
            s = sum(helper(processors[i]))
            index = i
    return index
def helper(p):
    arr = []
    for i in range(len(p)):
        arr.append(p[i][0])
    return arr