words = ["practice", "makes", "perfect", "coding", "makes"]
# word1 = "coding"
# word2 = "practice"

# word1 = "makes"
# word2 = "coding"

word1 = "makes"
word2 = "practice"

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if words is None or len(words) == 0:
            return -1

        diff = len(words) - 1
        shortest = 0
        pt1 = 0
        pt2 = 0

        for i, word in enumerate(words):
            if word == word1:
                pt1 = i

            elif word == word2:
                pt2 = i
            
            if abs(pt1-pt2) < diff:
                    shortest = abs(pt1-pt2)

        return shortest

if __name__ == '__main__':
    print(Solution().shortestDistance(words, word1, word2))


