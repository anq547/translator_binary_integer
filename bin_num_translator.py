def binnum(b):
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