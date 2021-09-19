def bin2num(b):
    x = -1
    y = 1
    ln = []
    lb_str = list(str(b))
    lb_int = []
    for i in lb_str:
        lb_int.append(int(i))

    while(abs(x) != len(lb_int) + 1):
        ln.append(lb_int[x] * y)
        x -= 1
        y *= 2

    return sum(ln)

def num2bin(b):
    def max_2_multiplier(x):
        y = 1
        while (y < x):
            y *= 2
        
        if y > x:
            return int(y / 2)
        
        else:
            return y
    
    l = []
    ls = []
    i = max_2_multiplier(b)

    while (i > 0):
        l.append(b // i)
        b = (b % i)
        i = i // 2

    for i in l:
        ls.append(str(i))

    bin = ''.join(ls)
    return int(bin)