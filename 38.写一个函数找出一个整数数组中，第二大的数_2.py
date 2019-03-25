def find_second_number(list):
    first=list[0]#存储最大值
    second=list[0]#存储第二大的值
    for i in range(1,len(list)):
        if list[i]>first:
            second=first
            first=list[i]
        elif list[i]>second:
            second=list[i]
    print('第二大的值为:',second)
list=[34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
find_second_number(list)