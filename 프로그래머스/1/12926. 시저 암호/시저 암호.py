def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if s[i] == " ":
            answer += " "
        else:
            alpha = ord(s[i]) + n
            if s[i].islower() and alpha > ord('z'):
                answer += chr(ord(s[i]) - 26 + n)
            elif s[i].isupper() and alpha > ord('Z'):
                answer += chr(ord(s[i]) - 26 + n)
            else:
                answer += chr(ord(s[i]) + n)

    return answer