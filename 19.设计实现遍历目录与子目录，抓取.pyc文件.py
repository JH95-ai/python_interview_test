import os
def get_path(name,suffix):
    list=[]
    for root,dirs,files in os.walk(name):
        for filename in files:
            name,suf=os.path.splitext(filename)
            if suf==suffix:
                list.append(os.path.join(root,filename))
    print(list)
get_path('./','.pyc')