# Last updated: 1/12/2026, 10:21:23 PM
class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
        