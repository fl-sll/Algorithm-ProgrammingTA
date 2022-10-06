height = int(input("Enter height of pyramid: "))

while height <= 0:
    print("Height cannot be negative or zero")
    height = int(input("Enter height of pyramid (>1): "))
else:
    for i in range(height+1):
        for j in range(i):
            print(i, end=" ")
        print(" ")