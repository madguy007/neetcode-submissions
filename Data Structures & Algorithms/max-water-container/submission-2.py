class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        res = 0

        while i < j:
            height = min(heights[i],heights[j])
            width = j-i
            vol = height*width
            res = max(res,vol)
            if heights[i] > heights[j]:
                j -= 1
            elif heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return res

            
 
            
