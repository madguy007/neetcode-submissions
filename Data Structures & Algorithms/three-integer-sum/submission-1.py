class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            target = (-1)*nums[i]
            while j < k:
                total = nums[j]+nums[k]
                if total > target:
                    k -=1
                elif total < target:
                    j += 1
                else:
                    res.add(tuple([nums[i],nums[j],nums[k]]))
                    k -= 1
                    j += 1
        return list(res)

        
            






        