class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        for i in nums:
            if i==c:
                c+=1
            else:
                return c
        return c