class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in hashmap:
                return [hashmap[remain],i]
            hashmap[nums[i]] = i
        return 
                



        