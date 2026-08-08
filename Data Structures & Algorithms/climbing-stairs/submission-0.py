class Solution:
    def climbStairs(self, n: int) -> int:
        if n ==1:
            return 1
        if n ==2:
            return 2
        current = 0 
        one = 1
        two = 2
        for i in range(3,n+1):
            current = one+two
            one = two
            two = current
        return current