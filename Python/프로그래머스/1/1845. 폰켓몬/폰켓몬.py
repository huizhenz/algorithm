def solution(nums):
    phonekemon = {}
    
    for n in nums:
        phonekemon[n] = phonekemon.get(n, 0) + 1
    
    return min(len(phonekemon), len(nums) // 2)