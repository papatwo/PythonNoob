import collections
class Solution:
    def findOcurrences(self, text, first, second):
        # text = text.split(' ')
        # res = []
        # for i in range(2,len(text)):
        #     if text[i-1] == second and text[i-2] == first:
        #         res.append(text[i])
        # return res
        

        ## Hash table method
        mapping = {}
        text = text.split( )

        for i in range(len(text)-2):
            key = (text[i], text[i+1])

            # setdefault(key[, default]) 
            # If key is in the dictionary, return its value. If not,
            # insert key with a value of default and return default.
            # default defaults to None.
        
            print(mapping.setdefault(key,[]).append(text[i+2]))

        find_key = (first, second)

        if find_key not in mapping:
            return []

        return mapping[find_key]



if __name__ == '__main__':
    # text = "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"
    # first = "kcyxdfnoa"
    # second = "jkypmsxd"
    # text = "ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv lnlqhmaohv lnlqhmaohv ypkk ypkk ypkk lnlqhmaohv lnlqhmaohv ypkk"
    # first = "lnlqhmaohv"
    # second = "ypkk"
    text = "alice is a good girl she is a good student"
    first = "a"
    second = "good"
    res = Solution().findOcurrences(text, first, second)
    print(res)