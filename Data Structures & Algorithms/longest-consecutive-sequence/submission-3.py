class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        c=0
        nums1 = set(nums)
        res=0
        for i in nums1:
            if i-1 not in nums1:
                c=1
                start = i
                while start+1 in nums1:
                    c+=1
                    start+=1
            res = max(c,res) 
        return res