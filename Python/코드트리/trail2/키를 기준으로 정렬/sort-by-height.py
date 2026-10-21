n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
temp = []
for i in range(n):
    temp.append((name[i], height[i], weight[i]))

temp.sort(key=lambda x: x[1])

for t in temp:
    n, h, w = t
    print(n, h, w)