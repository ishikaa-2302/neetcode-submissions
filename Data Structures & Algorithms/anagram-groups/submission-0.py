class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs1 = sorted(strs)
        result = []
        used = [False] * len(strs1)
        for i in range(len(strs1)):
            if used[i]:
                continue

            group = [strs1[i]]
            used[i] = True

            for j in range(i + 1, len(strs1)):
                if not used[j] and self.isAnagram(strs1[i], strs1[j]):
                    group.append(strs1[j])
                    used[j] = True
            result.append(group)
        return result

    def isAnagram(self,s,t):
        if len(s)!=len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True  