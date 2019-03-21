'''
Time:2019-3-2
Input:
    输入各个数字,以回车进行分割,输入0时输入结束
Output:
    输出输入数字的不重复个数
'''
list=[]  #定义一个列表
while True:
    a=input()  #输入数字
    if int(a)==0:#如果输入数字为0,输入结束
        break
    list.append(a)   #将输入的数字保存到列表中
a=set(list)  #将保存的数字运用set集合函数进行去重
for i in range(len(a)):  #计算set集合中数字的个数
    b=i+1
print(b)



