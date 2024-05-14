class Solution:
    def removeStars(self, s: str) -> str:
        retStr = []
        for c in s:
            if(c != '*'):
                retStr.append(c)
            else:
                retStr.pop()
        return ''.join(retStr)
