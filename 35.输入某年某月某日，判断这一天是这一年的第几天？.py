import datetime
year=input('请输入年份:')
month=input("请输入月份:")
day=input('请输入日期:')
day1=datetime.date(int(year),int(month),int(day))
day2=datetime.date(int(year),int(1),int(1))
print((day1-day2).days+1)