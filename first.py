print("Hello, World!")

def fib(n):
    first, second = 0, 1
    for _ in range(0, n):
        print(first)
        first, second = second, first + second

fib(int(input()))
