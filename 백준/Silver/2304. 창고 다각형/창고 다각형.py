n = int(input())
arr = [0]*1001
for i in range(n):
    l, h = map(int, input().split())
    arr[l] = h

# 가장 높은 기둥의 위치를 찾기 best_idx
Max = 0
best_idx = 0
for i in range(1001):
    if arr[i] > Max:
        Max = arr[i]
        best_idx = i

# 순회 시작할 인덱스 찾기 st_idx
st_idx = 0
for i in range(1001):
    if arr[i] != 0:
        st_idx = i
        break

# 역방향 순회 시작할 인덱스 찾기 ed_idx
ed_idx = 0
for i in range(1000, -1, -1):
    if arr[i] != 0:
        ed_idx = i
        break

# Sum 면적 저장
Sum = 0
# 왼쪽 st_idx -> best_idx
now_h = arr[st_idx]
for i in range(st_idx, best_idx+1):
    if now_h < arr[i]:
        now_h = arr[i]
    Sum += now_h

# 오른쪽 -> best_idx (역방향)
now_h = arr[ed_idx]
for i in range(ed_idx, best_idx, -1):
    if now_h < arr[i]:
        now_h = arr[i]
    Sum += now_h

print(Sum)