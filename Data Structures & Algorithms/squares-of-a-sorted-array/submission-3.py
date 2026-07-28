class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        pos = len(nums)-1
        res = [0]*len(nums)
        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                res[pos]=nums[left]*nums[left]
                left+=1
                pos-=1
            else:
                res[pos]=nums[right]*nums[right]
                pos-=1
                right-=1
        return res
