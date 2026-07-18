class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        result = 0
        max_f = 0
        for right in range(len(s)):
            if s[right] in freq:
                freq[s[right]]+=1
            else:
                freq[s[right]]=1
            max_f = max(max_f, freq[s[right]])
            if (right-left+1)-max_f>k:
                freq[s[left]]-=1
                left+=1
            result = max(result,right-left+1)
        return result