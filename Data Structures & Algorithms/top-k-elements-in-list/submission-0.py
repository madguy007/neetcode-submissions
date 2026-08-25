class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            counts[n] = 1 + counts.get(n,0)
        for n,c in counts.items():
            freq[c].append(n)
        
        res = list()
        for i in range(len(freq)-1,0,-1):
            for v in freq[i]:
                res.append(v)
                if len(res) == k:
                    return res


        