def myAtoi(s: str) -> int:
    number_string = ""
    prefix = 0
    for i in range(len(s)):
        if (number_string == "" and prefix == 0):
            if(s[i] == ' '):
                continue
            elif(s[i] == '-'):
                prefix = -1

            elif(s[i] == '+'):
                prefix = 1

            elif(s[i].isnumeric()):
                prefix = 1
                number_string += s[i]
            else:
                return 0
        else:
            if (s[i].isnumeric()):
                number_string += s[i]
            else:
                break

    if(number_string == ""):
        return 0
    number = int(number_string)
    if(number == 0):
        return 0

    if(prefix * number <= -2147483648):
        return -2147483648

    if(prefix * number >= 2147483648):
        return 2147483647

    return prefix * number

if __name__ == '__main__':
    print(myAtoi("42"))
    print(myAtoi("   -42"))
    print(myAtoi("4193 with words"))
    print(myAtoi("words and 4193"))
    print(myAtoi("-91283472332"))
    print(myAtoi("+-12"))