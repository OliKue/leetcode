class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p0 = 0
        p1 = 0
        isSub = True

        while (p0 < len(s) and p1 < len(t)):
            if (s[p0] == t[p1]):
                p0 += 1
                p1 += 1
            else:
                p1 += 1

        if (len(s) == 0):
            return True

        if (p0 == len(s) and s[p0 - 1] == t[p1 - 1]):
            return True
        else:
            return False
