class Solution:
    def reverseWords(self, s: str) -> str:
        list = []
        current_word = ""
        for c in s:
            if (c == ' '):
                if (len(current_word) > 0):
                    list.insert(0, current_word)
                current_word = ""
            else:
                current_word += c
        if (len(current_word) > 0):
            list.insert(0, current_word)
        return ' '.join(list)
