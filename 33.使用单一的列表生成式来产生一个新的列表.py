#该列表只包含满足以下条件的值，元素为原始列表中偶数切片
list_data = [1,2,5,8,10,3,18,6,20]
res = [x for x in list_data[::2] if x %2 ==0]
print(res)