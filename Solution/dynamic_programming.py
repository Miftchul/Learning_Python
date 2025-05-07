# Dynamic Programming Example: Fibonacci Sequence
# This program calculates the Fibonacci sequence using dynamic programming.
# It uses memoization to store previously computed values for efficiency.

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

def main():
    n = 10
    print(f"Fibonacci sequence up to {n}:")
    for i in range(n):
        print(fibonacci(i), end=" ")

if __name__ == "__main__":
    main()