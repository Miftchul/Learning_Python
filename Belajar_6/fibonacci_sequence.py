# Fibonacci sequence:
#  The Fibonacci sequence is a series of numbers in which each number is the sum of the two
#  preceding ones, usually starting with 0 and 1. In mathematical terms, it is defined by the
#  recurrence relation ( F(n) = F(n-1) + F(n-2) ), with initial conditions ( F(0) = 0 ) and ( F(1) = 1
#  ). The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. The Fibonacci sequence has
#  widespread applications in mathematics, computer science, nature, and art.

# Python program to display the Fibonacci sequence up to the 10th term

def recur_fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

ntersm = int(input("Enter the number of terms: "))

# check if the number of terms is valid
if ntersm <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(ntersm):
        print(recur_fibo(i))
