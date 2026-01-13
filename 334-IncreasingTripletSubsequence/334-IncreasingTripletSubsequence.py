# Last updated: 1/12/2026, 10:21:21 PM
class Solution(object):
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')


        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                    return True
        return False


        