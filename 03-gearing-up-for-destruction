def solution(pegs):
    # Your code here
    a = 1
    b = 0
    c = [0]
    for i in range(1, len(pegs)):
        a = -a
        b = pegs[i] - pegs[i-1] - b
        c.append(b)
        
    r = b*2.0/(1.0-2.0*a)
    valid = True
    
    s = 1
    for i in range(len(c)):
        if r*s + c[i] < 1:
            valid = False
            break
        s = -s
    
    if valid:
        en = abs(2*b)
        de = abs(1 - 2*a)
        
        x, y = de, en
        while x > 0:
            x, y = y%x, x
        return [en/y, de/y]
    else:
        return [-1, -1]
