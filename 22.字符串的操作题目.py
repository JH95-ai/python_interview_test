#全字母短句 PANGRAM 是包含所有英文字母的句子，
# 比如：A QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
# 定义并实现一个方法 get_missing_letter,
# 传入一个字符串采纳数，返回参数字符串变成一个 PANGRAM
# 中所缺失的字符。应该忽略传入字符串参数中的大小写，
# 返回应该都是小写字符并按字母顺序排序
# （请忽略所有非 ACSII 字符）
def get_missing_letter(a):
    s1=set('abcdefghijklmnopqrstuvwxyz')
    s2=set(a)
    ret=''.join(sorted(s1-s2))
    return ret
print(get_missing_letter('python'))