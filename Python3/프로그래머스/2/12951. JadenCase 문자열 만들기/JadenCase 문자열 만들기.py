def solution(s):
    new_s = ""
    for i in range(len(s)):
        if s[i] == " ":
            new_s += " "
        elif i == 0 and s[i].isalpha() or s[i-1] == " " and s[i].isalpha():
            new_s += s[i].upper()
        else:
            new_s += s[i].lower()
    return new_s