def missingInteger(nums: list[int]) -> int:
    prefix = list()
    for i in range(len(nums)):
        if(len(prefix) == 0):
            prefix.append(nums[i])
        elif(prefix[-1] +1 == nums[i]):
            prefix.append(nums[i])
        else:
            break

    summe = 0
    for num in prefix:
        summe += num

    i = 0
    while i < len(nums):
        if(nums[i] == summe):
            summe = nums[i] + 1
            i = 0
        else:
            i += 1

    return summe


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(missingInteger([1, 2, 3, 2, 5]))
    print(missingInteger([3,4,5,1,12,14,13]))
    print(missingInteger([29,30,31,32,33,34,35,36,37]))
    print(missingInteger([47, 48, 49, 9, 3, 8, 1, 9, 2, 5, 4, 5, 9]))
    print(missingInteger([1, 2, 3, 9, 2, 10, 8, 3, 10, 2]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
