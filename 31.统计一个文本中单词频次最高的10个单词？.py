import re
def text(filepath):
    dictword={}
    with open(filepath) as f :
        for line in f :
            line =re.sub('\W+',' ',line)
            lineone=line.split()
            for key in lineone:
                if not dictword.get(key):
                    dictword[key]=1
                else:
                    dictword[key]+=1
    num_ten=sorted(dictword.items(),key=lambda x:x[1],reverse=True)[:10]
    num_ten=[x[0] for x in num_ten]
    return num_ten