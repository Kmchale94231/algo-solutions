# Last updated: 1/8/2026, 11:32:10 AM
1class Solution(object):
2    def gcdOfStrings(self, str1, str2):
3        while str1 + str2 == str2 + str1:
4        
5            def gcd(a, b):
6                while b != 0:
7                    a, b = b, a % b
8                return a    
9            x = gcd(len(str1), len(str2))
10            
11            return str1[0:x]
12        else:
13            return ""