#给定一个整数数组和一个目标值，
#找出数组中和为目标值的两个数。
#你可以假设每个输入只对应一种答案，
#且同样的元素不能被重复利用。
#示例:给定nums = [2,7,11,15],target=9
#因为 nums[0]+nums[1] = 2+7 =9,所以返回[0,1]
class Solution:
    def twonum(self,nums,target):
        size=0
        d={}
        while size<len(nums):
            if target-nums[size] in d :
                if d[target-nums[size]] <size:
                    return [d[target-nums[size]],size]
            else:
                d[nums[size]]=size
                size=size+1
solution=Solution()
list=[2,7,11,19]
target=13
nums=solution.twonum(list,target)
print(nums)