def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

happy_numbers = []

for num in range(1, 100):
    if is_happy_number(num):
        happy_numbers.append(num)
        
print("Happy numbers between 1 and 100:")
print(happy_numbers)

