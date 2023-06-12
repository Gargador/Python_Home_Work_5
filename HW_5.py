# Задача 26:
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)
        
a = int(input())
b = int(input())
print(power(a, b))


# Задача 28:
def sum(a, b):
    if b == 0:
        return a
    elif b > 0:
        return sum(a+1, b-1)
    else:
        return sum(a-1, b+1)

a, b = map(int, input().split())
print(sum(a, b))
