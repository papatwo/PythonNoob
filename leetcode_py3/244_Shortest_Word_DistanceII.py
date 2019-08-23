from collections import defaultdict

class WordDistance:

    def __init__(self, words):

        self.locations = defaultdict(list)

        for i, w in enumerate(words):
            self.locations[w].append(i)

    def shortest(self, word1, word2):
        loc1, loc2 = self.locations[word1], self.locations[word2]
        pt1, pt2 = 0, 0
        min_dist = float("inf")

        while pt1 < len(loc1) and pt2 < len(loc2):
            min_dist = min(min_dist, abs(loc[pt1] - loc[pt2]))
            if loc1[pt1] < loc2[pt2]:
                pt1 += 1
            else:
                pt2 += 1

        return min_dist


if __name__ == '__main__':
    word1 = WordDistance("coding")
    word2 = WordDistance("practice")
    print(word2)
    # print(WordDistance.shortest(word1, word2))