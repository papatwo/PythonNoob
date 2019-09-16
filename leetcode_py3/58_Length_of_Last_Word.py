class Solution:
    def lengthOfLastWord(self, s):
        # count = 0
        # len_count = 0
        # for i in range(len(s)):
        #     if s[i] == ' ':
        #         len_count = 0
        #     else:
        #         len_count += 1
        #         count = len_count
        # return count
                
        
        if not s:
            return 0
        else:
            words = s.split(" ")
            for i in range(len(words)-1,-1,-1):
                if words[i].isalpha():
                    return len(words[i])
            return 0

if __name__ == '__main__':
    s = "Hello World"
    print(Solution().lengthOfLastWord(s))


'''

Given a string s consists of upper/lower-case alphabets and empty space
characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

Example:

Input: "Hello World" Output: 5

'''
                    
        