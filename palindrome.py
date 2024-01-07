def isPalindrome(s: str) -> bool:
    def return_string():
        alphabets = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        ]
        new_string = ""
        for i in s:
            if i.lower() in alphabets:
                new_string += i.lower()
        return new_string

    s = return_string()
    if len(s) <= 1:
        return True

    if len(s) % 2 == 0:
        string1 = s[0 : len(s) // 2]
        string2 = s[len(s) // 2 :][::-1]
        print(string1, string2)
        return string1 == string2

    else:
        string1 = s[0 : len(s) // 2]
        string2 = s[len(s) // 2 + 1 :][::-1]
        return string1 == string2


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("deed"))
print(isPalindrome("0P"))
