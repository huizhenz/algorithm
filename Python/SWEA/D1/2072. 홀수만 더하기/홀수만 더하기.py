T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
               
    Sum = 0
    for i in range(len(arr)):
    	if arr[i] % 2 != 0:
        	Sum += arr[i]       		
    print(f"#{tc}", Sum)