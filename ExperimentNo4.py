# Experiment No. 4
# Calculate the nth Fibonacci number efficiently

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


# Main program
n = int(input("Enter the value of n: "))

result = fibonacci_iterative(n)

print("The", n, "th Fibonacci number is:", result)
