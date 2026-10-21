A = input()

# Please write your code here.
answer = 0
stack = []
for i in range(len(A)):
    if A[i] == '(':
        stack.append(i)
    for j in range(i+1, len(A)):
        if stack and A[j] == ')':
            answer += 1
    stack = []

print(answer)