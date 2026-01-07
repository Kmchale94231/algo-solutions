# Last updated: 1/7/2026, 9:25:35 AM
class Solution(object):
    def largestUniqueNumber(self, nums):
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
    
        curr_unique = -1
    
        for num, value in count.items():
            if value == 1:
                curr_unique = max(curr_unique, num)
        return curr_unique
    
            
        
        
        