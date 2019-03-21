c=input().split(' ')
a=int(c[0])
b=int(c[1])
m=[]*a
n=[]*b
list1=input().split(' ')
for i in range(a):
    m.append(int(list1[i]))
list2=input().split(' ')
for i in range(b):
    n.append(int(list2[i]))
m=sorted(m)
n=sorted(n)
for i in range(len(m)):
    for j in range(len(n)):
        if m[i]==n[j]:
            print(m[i])