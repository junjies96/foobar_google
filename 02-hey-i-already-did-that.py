def getNext(n, b):
    nums = sorted(n)
    diff = []
    minus = 0
    for i in range(len(n)):
        diff.append(str((b + int(nums[i]) - minus - int(nums[-1-i]))%b))
        minus = int(int(nums[i]) < int(nums[-i-1]) + minus)
    return ''.join(diff[::-1]).zfill(len(n))
    
def solution(n, b):
    #Your code here
    id = {}
    count = 0
    while n not in id:
        id[n] = count
        count += 1
        n = getNext(n, b)
        print n
    return count - id[n]
