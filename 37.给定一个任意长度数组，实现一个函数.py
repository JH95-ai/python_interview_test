#让所有奇数都在偶数前面，而且奇数升序排列，偶数降序排序，
# 如字符串'1982376455',变成'1355798642'
def test(l):
    if isinstance(l,str):
        l=[int(i) for i in l]
    l.sort(reverse=True)
    for i in range(len(l)):
        if l[i]%2>0:
            l.insert(0,l.pop(i))
    print(''.join(str(e) for e in l))
l='1234567865432123456'
test(l)