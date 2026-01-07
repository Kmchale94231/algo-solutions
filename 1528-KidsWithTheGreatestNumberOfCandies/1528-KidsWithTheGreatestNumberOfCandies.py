# Last updated: 1/7/2026, 1:19:25 PM
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_candy = max(candies)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                candies[i] = True
            else:
                candies[i] = False
        return candies