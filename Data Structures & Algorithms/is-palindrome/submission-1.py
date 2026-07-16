class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split())
        s = s.lower()
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch
        return clean == clean[::-1]