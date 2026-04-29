def solution(s):
    string = s.split(' ')
    answer = []
    for i in range(len(string)):
        new_s = ''
        for j in range(len(string[i])):
            if j % 2 == 0:
                new_s += string[i][j].upper()
            else:
                new_s += string[i][j].lower()
        answer.append(new_s)
    return ' '.join(answer)