class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        post = [1]*len(nums)

        for i in range(1,len(nums)):
            j = -i-1
            pre[i] = pre[i-1]*nums[i-1]
            post[j] = post[j+1]*nums[j+1]

        res = [x*y for x,y in zip(pre,post)]
        return res
        



        
       
        