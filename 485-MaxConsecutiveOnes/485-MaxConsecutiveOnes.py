# Last updated: 1/28/2026, 5:39:53 PM
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        
        count = 0
        max_consec = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            max_consec = max(max_consec, count)
        return max_consec
            
            
            
                
                
