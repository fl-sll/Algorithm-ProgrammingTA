time = int(input("Enter the number of seconds: "))

hour = time // 3600
minute = time // 60
second = time % 60

time_total = f"{hour}:{minute}:{second}"

print("Results: " + time_total)