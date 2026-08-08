class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        c=0
        while i>=0 and s[i]==" ":
            i-=1
        while i>=0 and s[i]!=' ':
            i-=1
            c+=1
        return c