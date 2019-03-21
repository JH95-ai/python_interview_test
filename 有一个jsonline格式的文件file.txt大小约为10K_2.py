from mmap import mmap
def roadbigfile(fp):
    with open(fp,'r+') as f:
        m=mmap(f.fileno(),0)
        tmp=0
        for i,char in enumerate(m):
            if char==b:
                yield m[tmp:i+1].decode()
                tmp=i+1
if __name__=='__main__':
    for i in roadbigfile('big_file'):
        print(i)