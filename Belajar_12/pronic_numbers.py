#  A pronic number, also known as an oblong number or rectangular number, is a type of
#  figurate number that represents a rectangle. It is the product of two consecutive integers, n
#  and (n + 1). Mathematically, a pronic number can be expressed as:
#  𝑃𝑛 = 𝑛∗(𝑛+1)
#  For example, the first few pronic numbers are
#  P1 = 1∗(1+1) = 2
#  𝑃2 = 2∗(2+1) = 6
#  𝑃3 = 3∗(3+1) = 12
#  𝑃4 = 4∗(4+1) = 20

def is_pronic_number(num):
    for n in range(num + 1):
        if n * (n + 1) == num:
            return True
    return False

print("Pronic bumbers between 1 and 100 are: ")
for i in range(1, 100):
    if is_pronic_number(i):
        print(i, end=" | ")