def solution(s):
    dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    prev = ""
    answer = ""
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            prev += s[i]
            
            if dict.get(prev):
                answer += dict[prev]
                prev = ""
    return int(answer)
        
        
        
        
        
    