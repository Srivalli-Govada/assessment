def solve(n1):
    sign = '-' if n1<0 else ''
    n1 = abs(n1)
    if n1 < 3:
        return str(n1)
    s=''
    while n1 != 0:
        s = str(n1%3) + s
        n1 = n1//3
        return sign+s
n1=int(input())
print(solve(n1))
