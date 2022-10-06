lower_bound = int(input("Enter lower bound: "))

even_numbers = []
odd_numbers = []

while lower_bound < 0:
    print("lower bound is too small")
    lower_bound = int(input("Enter lower bound: "))
else:
    upper_bound = int(input("Enter upper bound: "))
    for i in range(lower_bound, upper_bound + 1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

print(f"The even numbers are: {even_numbers}")
print(f"The odd numbers are: {odd_numbers}")