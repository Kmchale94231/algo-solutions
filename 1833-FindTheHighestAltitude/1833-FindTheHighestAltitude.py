# Last updated: 1/20/2026, 11:36:23 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefix_sum = 0
        max_sum = 0

        for i in range(len(gain)):
            prefix_sum += gain[i]
            max_sum = max(max_sum, prefix_sum)
        return max_sum