list1 = [10,20,30,40]
list2 = [100,200,300,400]
list2_rev = []

for i in list2:
    list2_rev.insert(0,i)

list3 = []

for j in range(0, len(list1)):
    list3.append(str(list1[j]) + " " + str(list2_rev[j]))

for k in list3:
    print(k)