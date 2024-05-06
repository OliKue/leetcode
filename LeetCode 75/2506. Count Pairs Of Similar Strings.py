class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # First approach solution

        # list_of_sets = []
        # for word in words:
        #     char_set = set()
        #     for char in word:
        #         char_set.add(char)
        #     list_of_sets.append(char_set)

        # # print(list_of_sets)
        # # n squared

        # number = 0
        # for p1 in range(0, len(list_of_sets)):
        #     for p2 in range(p1 + 1, len(list_of_sets)):
        #         if(list_of_sets[p1] == list_of_sets[p2]):
        #             number +=1

        # best runtime solution
        map_of_sets = {}
        for word in words:
            frozen = frozenset(word)

            if (frozen in map_of_sets):
                map_of_sets[frozen] += 1
            else:
                map_of_sets[frozen] = 1

        number = 0
        for num in map_of_sets.values():
            if num == 1:
                continue
            while num != 0:
                number += num - 1
                num -= 1

        return number