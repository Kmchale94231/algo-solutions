class Solution(object):
    def reverseVowels(self, s):
        l = 0
        r = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        letter = list(s)

        while l < r:
            if letter[l].lower() not in vowels:
                l += 1
            if letter[r].lower() not in vowels:
                r -= 1
            if letter[l].lower() in vowels and letter[r].lower() in vowels:
                letter[l], letter[r] = letter[r], letter[l]
                l += 1
                r -= 1
                
        return "".join(letter)      