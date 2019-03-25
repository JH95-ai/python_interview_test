#使用counter中的most_common方法
import re
from collections import Counter
def text2(filepath):
    with open(filepath) as  f:
        return list(map(lambda x:x[0],Counter(re.sub('\W+',' ',f.read()).split()).most_common(10)))