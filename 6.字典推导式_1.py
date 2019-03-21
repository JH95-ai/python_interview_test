'''
Time:2019-3-11
'''
#列表推导式,例1
multiple=[i for i in range(30) if i%3==0]
print(multiple)
#例2
def squrted(x):
    return x*x
multiple2=[squrted(i) for i in range(30) if i%3==0]
print(multiple2)
#例3
multiple3=(i for i in range(30) if i%3==0)
print(type(multiple3))

#字典推导式
#大小写key合并
print('--------字典推导式----------')
mscase={'a':6,'b':7,'A':4,'Z':2}
mscase_frequency={
    k.lower():mscase.get(k.lower(),0)+mscase.get(k.upper(),0)
    for k in mscase.keys()
        if k.lower() in ['a','b']
}
print(mscase_frequency)
#快速更换键和值
test1={'x':3,'y':4}
test1_frequency={
    x:v for v,x in test1.items()
}
print(test1_frequency)
#集合推导式
squared={x**2 for x in [1,1,2]}
print(squared)