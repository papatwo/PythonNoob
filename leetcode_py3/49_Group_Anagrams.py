class Solution:
    def groupAnagrams(self, strs):
        letter_dict = {}
        res = []
        
        for word in strs:
            letters = tuple(sorted(list(word)))
            if letters in letter_dict:
                letter_dict[letters].append(word)
            else:
                letter_dict[letters] = [word]
        
        for key in letter_dict:
            res.append(letter_dict[key])
            
        return res

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))

'''

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

'''
            