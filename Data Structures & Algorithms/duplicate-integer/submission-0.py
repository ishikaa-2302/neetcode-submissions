class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        flag = 0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==0:
                return True
        return False