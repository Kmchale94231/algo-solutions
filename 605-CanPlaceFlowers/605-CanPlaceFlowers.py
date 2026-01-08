# Last updated: 1/8/2026, 12:11:50 PM
1class Solution(object):
2    def reverseWords(self, s):
3        return " ".join(s.split()[::-1])
4        