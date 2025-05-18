# Input the interval from the user
lower = int(input("Enter lower limit the interval: "))
upper = int(input("Enter upper limit the interval: "))

for num in range(lower, upper + 1):
    order = len(str(num))
    temp_num = num
    sum = 0
    
    while temp_num > 0:
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
        
    # Check if "num" is an Armstrong number
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number") 
