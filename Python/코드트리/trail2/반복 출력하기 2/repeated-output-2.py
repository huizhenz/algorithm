n = int(input())

# Please write your code here.
def print_str(i):
    if i == n:
        return
    
    print_str(i+1)
    print("HelloWorld")

print_str(0)