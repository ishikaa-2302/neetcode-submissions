class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        c_0 = 0
        for i in range(len(nums)):
            if nums[i]==0:
                c_0+=1
            else:
                prod = prod*nums[i]
        res=[]
        for i in range(len(nums)):
            if c_0==1 and nums[i]!=0:
                res.append(0)
            elif c_0==1 and nums[i]==0:
                res.append(prod)
            elif c_0>1:
                res.append(0)
            else:
                res.append(prod//nums[i])
        return res