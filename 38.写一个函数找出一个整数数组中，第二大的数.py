def find_second_number(list):
    list.sort(reverse=False)
    print(list)
    list_change=list[-2]
    print(list_change)
list=[34, 11, 23, 56, 78, 0, 9, 12, 3, 7, 5]
find_second_number(list)