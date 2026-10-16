def solution(nums):
    temp = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                temp.append([i, j, k])
    
    answer = 0
    for t in temp:
        cnt = 0
        i, j, k = t
        sum = nums[i] + nums[j] + nums[k]
        
        for s in range(1, int(sum ** 0.5)+1):
            if sum % s == 0:
                    cnt +=1
        
        if cnt == 1:
            answer += 1
    
    return answer