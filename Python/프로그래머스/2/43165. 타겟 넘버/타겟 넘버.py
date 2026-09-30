def solution(numbers, target):
    def dfs(i, total):
        if i == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        
        plus = dfs(i + 1, total + numbers[i])
        minus = dfs(i + 1, total - numbers[i])
        return plus + minus
        
    return dfs(0,0)