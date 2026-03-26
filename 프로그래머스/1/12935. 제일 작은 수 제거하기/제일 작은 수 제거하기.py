def solution(arr):
    min_idx = arr.index(min(arr))
    arr.pop(min_idx)
    
    if not arr:
        arr = [-1]
    return arr