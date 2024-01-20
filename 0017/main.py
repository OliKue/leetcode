def letterCombinations(digits: str) -> list[str]:
    number_mapping = {'2': {'a', 'b', 'c'}, '3': {'d', 'e', 'f'}, '4': {'g', 'h', 'i'},
                      '5': {'j', 'k', 'l'}, '6': {'m', 'n', 'o'}, '7': {'p', 'q', 'r', 's'},
                      '8': {'t', 'u', 'v'}, '9': {'w', 'x', 'y', 'z'}}

    if (len(digits) == 0):
        return []

    return_list = [""]
    for i in range(len(digits)):
        letters = number_mapping[digits[i]]

        permuted = []
        for to_permute in return_list:
            for letter in letters:
                permuted.append(to_permute + '' + letter)

        return_list = permuted

    return return_list

if __name__ == '__main__':
    print(letterCombinations('23'))
