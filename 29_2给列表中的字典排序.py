#假设有如下list对象，
# alist=[{"name":"a","age":20},
# {"name":"b","age":30},
# {"name":"c","age":25}],
# 将alist中的元素按照age从大到小排序
# alist=[{"name":"a","age":20},
# {"name":"b","age":30},
# {"name":"c","age":25}]
alist=[{"name":"a","age":20}, {"name":"b","age":30}, {"name":"c","age":25}]
alist_sorted=sorted(alist,key=lambda e:e.__getitem__("age"),reverse=True)
print(alist_sorted)