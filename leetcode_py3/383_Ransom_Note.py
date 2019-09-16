class Solution:
    def canConstruct(self, ransomNote, magazine):
        checkmap = {}
        for s in ransomNote:
            if s in checkmap:
                checkmap[s] += 1
            else: 
                checkmap[s] = 1
        
        for s in magazine:
            if s in checkmap:
                checkmap[s] -= 1
        
        for key in checkmap:
            if checkmap[key] > 0:
                return False
                
        return True
        
        
if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "ab"
    print(Solution().canConstruct(ransomNote, magazine))


'''

Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note: You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''