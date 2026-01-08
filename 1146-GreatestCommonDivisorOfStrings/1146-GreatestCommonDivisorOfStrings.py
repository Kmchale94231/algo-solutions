# Last updated: 1/8/2026, 11:32:32 AM
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        while str1 + str2 == str2 + str1:
        
            def gcd(a, b):
                while b != 0:
                    a, b = b, a % b
                return a    
            x = gcd(len(str1), len(str2))
            
            return str1[0:x]
        else:
            return ""