class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_p = 0
        w2_p = 0
        new_word = ""
        take_w1 = True
        while w1_p <= len(word1) - 1 and w2_p <= len(word2) - 1:
            print("p1:", w1_p, " p2:", w2_p)
            if (take_w1):
                new_word += word1[w1_p]
                take_w1 = False
                w1_p += 1
                if (w1_p >= len(word1)):
                    new_word += word2[w2_p:]
                    return new_word
            else:
                new_word += word2[w2_p]
                take_w1 = True
                w2_p += 1
                if (w2_p >= len(word2)):
                    new_word += word1[w1_p:]
                    return new_word

        return new_word