class Solution:
    def reverseWords(self, s):
        if not s:
            return s
        
        words = s.split(" ") # should use s.split
        no_space = []
        for word in words:
            if word != "":
                no_space.append(word)
        
        for i in range(len(no_space)-1, -1, -1):
            if i != 0:
                res = res + no_space[i] + " "
            elif i == 0:
                res += no_space[i]
        return res
        
        
#         res = ""
#         words = s.split() 
#         if words == []:
#             return ""
        
#         for i in range(len(words)-1, 0, -1):
#                 res = res + words[i] + " "

#         res += words[0]
#         return res


if __name__ == '__main__':
    s = "a good   example"
    print(Solution().reverseWords(s))


'''

Given an input string, reverse the string word by word.

 

Example 1:

Input: "the sky is blue" Output: "blue is sky the" Example 2:

Input: "  hello world!  " Output: "world! hello" Explanation: Your reversed
string should not contain leading or trailing spaces. Example 3:

Input: "a good   example" Output: "example good a" Explanation: You need to
reduce multiple spaces between two words to a single space in the reversed
string.
 

Note:

A word is defined as a sequence of non-space characters. Input string may
contain leading or trailing spaces. However, your reversed string should not
contain leading or trailing spaces. You need to reduce multiple spaces between
two words to a single space in the reversed string.


'''
        
        
        
      