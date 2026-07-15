class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        result = []
        pairs = list(freq.items())
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        for i in range(k):
            result.append(pairs[i][0])
        return result