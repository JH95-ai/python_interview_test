str='k:1|k1:2|k2:3|k3:4'
def strdict(str):
    dict={}
    for items in str.split('|'):
        key,value=items.split(':')
        dict[key]=value
    return dict
d={k:int(v) for t in str.split('|') for k,v in (t.split(":"),)}
print(d)