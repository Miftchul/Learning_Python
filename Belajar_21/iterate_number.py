# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n

class DivisibleBy7:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 7 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration
    
# Example usage
n = int(input("Enter a number: "))
divisible_by_7 = DivisibleBy7(n)
for number in divisible_by_7:
    print(number)
    