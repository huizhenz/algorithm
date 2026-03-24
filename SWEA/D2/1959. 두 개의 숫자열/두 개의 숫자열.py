T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    if n <= m:
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
    else:
        n, m = m, n
        arr2 = list(map(int, input().split()))
        arr1 = list(map(int, input().split()))
 
    def match_max(sliced_arr):
        Sum = 0
        for i in range(len(sliced_arr)):
            Sum += arr1[i] * sliced_arr[i]
        return Sum
 
    idx = abs(n-m) + 1
    Max = -21e8
    for i in range(idx):
        ret = match_max(arr2[i:n+i])
        if Max < ret:
            Max = ret
 
    print(f"#{test_case} {Max}")