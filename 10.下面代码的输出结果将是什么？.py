'''
TIME:2019-3-12
'''
list = ['a','b','c','d','e']
print(list[10:])
#尝试获取list[10]和之后的成员，
# 会导致IndexError。然而，尝试获取列表的切片，
# 开始的index超过了成员个数不会产生IndexError，而是仅仅返回一个空列表。
