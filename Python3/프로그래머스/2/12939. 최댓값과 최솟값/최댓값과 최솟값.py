def solution(s):
    num = list(map(int, (s.split())))
    answer = f"{min(num)} {max(num)}"
    return answer