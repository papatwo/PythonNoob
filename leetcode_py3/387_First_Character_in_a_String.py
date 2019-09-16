class Solution:
    def firstUniqChar(self, s):
        if not s:
            return -1
        smap = {}
        for ch in s:
            if ch in smap:
                smap[ch] += 1
            else:
                smap[ch] = 1
        print(smap)
        for i,key in enumerate(smap):
            if smap[key] == 1:
                return s.index(key)
        return -1
        

if __name__ == '__main__':
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))


'''

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

s = "leetcode" return 0.

s = "loveleetcode", return 2.

'''