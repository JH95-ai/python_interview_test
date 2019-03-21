class solution():
    def reversed(self,x):
        if -10<x<10:
            return x
        str_x=str(x)
        if str_x[0]!='-':
            str_x=str_x[::-1]
            x=int(str_x)
        else:
            str_x=str_x[1:][::-1]
            str_x=int(str_x)
            x=-str_x
        return x
if __name__=="__main__":
    a=solution()
    b=a.reversed(-1234)
    print(b)