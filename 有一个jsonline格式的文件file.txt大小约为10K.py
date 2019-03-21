from multiprocessing import Process
def roadtxt():
    with open('file.txt','rb')as f:
        return f.readlines()
if __name__=='__main__':
    for e in roadtxt():
        Process(e)
