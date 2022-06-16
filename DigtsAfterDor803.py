ns = [int(i) for i in input().split(" ")]
def convert(numerator, denominator):
    ans= str(numerator//denominator)+ "."
    l={}
    index=0
    numerator = numerator%denominator
    l[numerator]=index
    t=False
    while t==False:
        if numerator==0:
            break
        digit = numerator*10//denominator
        numerator=numerator*10-(numerator*10//denominator)*denominator
        if numerator not in l:
            ans+=str(digit)
            index+=1
            l[numerator]=index
            t=False
        else:
            ans+=str(digit)+")"
            ans=ans[:l.get(numerator)+len(ans[:ans.index(".")+1])]+"("+ ans[l.get(numerator)+len(ans[:ans.index(".")+1]):]
            t=True
    return ans
deep = 2000000
def longPeriod(a):
    if not a.__contains__("("):
        return str(float(a)).ljust(deep, '0')
    n = str(a)
    i = str(n).index("(")
    n = n[i:]
    nc = n[:]
    n = n.lstrip("(").rstrip(")")
    a = str(a).replace(nc, "")
    while len(a) < deep:
        a += n
    return a[0:deep]

dv = convert(ns[0], ns[1])
s = longPeriod(dv)
s = s[s.index('.') + 1:]
print(s[ns[2]-1])