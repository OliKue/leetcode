class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        i = 0
        while (i < len(asteroids)):
            # add if stack is empty
            if (len(stack) == 0):
                stack.append(asteroids[i])
                i += 1
            # check top if stack not empty
            else:
                top = stack.pop(-1)
                isTopNegative = top < 0
                isNextNegative = asteroids[i] < 0

                if (isTopNegative):
                    stack.append(top)
                    stack.append(asteroids[i])
                    i += 1
                elif (isNextNegative):
                    if (abs(top) > abs(asteroids[i])):
                        stack.append(top)
                        i += 1
                    elif (abs(top) == abs(asteroids[i])):
                        i += 1
                else:
                    stack.append(top)
                    stack.append(asteroids[i])
                    i += 1

        return stack