# Last updated: 1/7/2026, 9:25:35 AM
class Solution(object):
    def maxNumberOfBalloons(self, text):
        text_dict = {}
        word = 'balloon'
        
        for char in text:
            if char in text_dict:
                text_dict[char] += 1
            else:
                text_dict[char] = 1
                
        if any(char not in text_dict for char in word):
            return 0
        else:
            return min(text_dict['b'], text_dict['a'], text_dict['l']//2, text_dict['o']//2, text_dict['n'])
            
            
                
        
            
        
        
                
            
        