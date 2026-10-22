n = int(input())

# Please write your code here.
temp = []
def print_n(i):
    if i == n + 1:
        return
    
    temp.append(i)
    print_n(i + 1)
    temp.append(i)

print_n(1)

for i in range(len(temp)):
    print(temp[i], end=" ")
    if i == n-1:
        print()