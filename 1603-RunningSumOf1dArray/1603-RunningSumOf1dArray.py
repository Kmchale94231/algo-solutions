# Last updated: 1/7/2026, 9:25:32 AM
class Solution(object):
    def runningSum(self, nums):
        running_sum = []
        total = 0
        
        
        for i in nums:
            total += i
            running_sum.append(total)
        
        return running_sum
                        
        