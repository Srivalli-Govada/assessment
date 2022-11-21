def find(n):
    q=n/3
    r=n%3
    if q==0:
        return ''
    else:
        return find(int(q))+str(int(r))
n=int(input())
print(find(n))
