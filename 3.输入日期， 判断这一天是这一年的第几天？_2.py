import datetime
year=input('请输入年份:')
month=input('请输入月份:')
day=input("请输入日期:")
year1=datetime.date(int(year),int(month),int(day))
year2=datetime.date(int(year),int(1),int(1))
a=(year1-year2).days+1
print(a)
