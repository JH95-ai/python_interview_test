class Car:
    def __init__(self,name,loss):#loss为一个数组,loss[0,3]依次为价位,油耗,公里数
        self.name=name
        self.loss=loss
    def getname(self):
        return self.name
    def getloss(self):
        return self.loss[1]*self.loss[2]
BMW=Car('宝马',[60,6,500])
print(getattr(BMW,'name'))
print(dir(BMW))