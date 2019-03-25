def atoi(s):
    num=0
    for v in s:
        for j in range(10):
            if v==str(j):
                num=num*10+j
    return num
#利用ord函数
def atoi(s):
    num=0
    for v in s :
        num=num*10 +ord(v)-ord('0')
    return num

