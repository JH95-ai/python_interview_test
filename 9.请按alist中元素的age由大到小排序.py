alist = [{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]
def sorted1(alist):
    return sorted(alist,key=lambda x:x['age'],reverse=True)
a=sorted1(alist)
print(a)
a=[5,7,6,3,4,1,2]
b=sorted(a) #保留原列表
print(b)
L=[('b',2),('a',1),('c',3),('d',4)]
l1=sorted(L,key=lambda x:x[0])#利用cmp函数
print(l1)