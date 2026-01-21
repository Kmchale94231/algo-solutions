# Last updated: 1/20/2026, 11:36:24 PM
class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        l, count, res = 0, 0, 0

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1

            if r - l + 1 > k:
                if s[l] in vowels:
                    count -= 1
                l += 1
            res = max(res, count)
        return res
        
        





        