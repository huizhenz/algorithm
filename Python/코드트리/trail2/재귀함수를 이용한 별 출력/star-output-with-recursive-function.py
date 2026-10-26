n = int(input())

# Please write your code here.
def start(i):
    if i == n+1:
        return
    
    print('*' * i)
    start(i+1)

start(1)