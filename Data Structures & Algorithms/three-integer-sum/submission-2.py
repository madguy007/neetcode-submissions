class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums)-1
            target = (-1)*nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                total = nums[j]+nums[k]
                if total > target:
                    k -=1
                elif total < target:
                    j += 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                   
        return res

        
            






        