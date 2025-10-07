class Solution(object):
    def getAverages(self, nums, k):
        n = len(nums)
        ans = [-1] * n
        window_size = 2 * k + 1
        
        if k == 0:
            return nums
        if window_size > n:
            return ans
        
        window_sum = sum(nums[:window_size])
        ans[k] = window_sum // window_size

        for i in range(window_size, n):
            window_sum = window_sum - nums[i - window_size] + nums[i]
            ans[i-k] = window_sum // window_size
        return ans
        
        
            
            
            
            
            
            
            
            
        
        
        
        
        