bill = float(input("Enter amount of bill: "))
num_of_people = int(input("Enter number of people: "))
tip = float(input("Enter amount of tip (%): "))

tip_amount = (tip/100) * bill
tip_person = tip_amount / num_of_people

total_amount = (bill / num_of_people) + tip_person

print("Tip amount per person $" + "{:.2f}".format(tip_person))
print("Total amount per person $" + "{:.2f}".format(total_amount))