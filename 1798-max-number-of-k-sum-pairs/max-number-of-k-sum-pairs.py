class Solution(object):
    def maxOperations(self, nums, k):
        my_list = sorted(nums)
        l, r = 0, len(nums) - 1
        count = 0

        while l < r:
            if my_list[l] + my_list[r] == k:
                count += 1
                l += 1
                r -= 1 
            elif my_list[l] + my_list[r] > k:
                r -= 1 
            else:
                l += 1
        return count
                

        