class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        current = ""

        for ch in s:
            if ch not in current:
                current = current+ch
            else:
                current = current[current.index(ch) + 1:] + ch
            max_len = max(max_len, len(current))
        return max_len
