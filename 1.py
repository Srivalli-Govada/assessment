class sol:
  def solve(self,n):
    s1='-' if n<0 else ''
    n=abs(n)
    if(n<3):
      return str(n)
    s=''
    while n!=0:
      s=str(n%3)+s
      n=n//3
    return s1+s
n1=int(input)
a=sol()
print(a.solve(n1))
