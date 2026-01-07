# Last updated: 1/7/2026, 9:25:37 AM
class Solution(object):
    def sortedSquares(self, nums):
        
        l, r = 0, len(nums) - 1 
        ans = [0] * len(nums)
        i = -1
        
        while l <= r:
            left = nums[l] * nums[l]
            right = nums[r] * nums[r]
            
            if left > right:
                ans[i] = left
                l += 1
                
            else:
                ans[i] = right
                r -= 1
            i -= 1
        return ans
        
                
            
            
        