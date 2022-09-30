
# ! git commands
# // initialize repo

# // adding file

# // checking status

# // committing

# // pushing



#? lists
#// ordered, indexed, mutable, allows duplicates
x = [1, "hello", 2.5];
# print(len(x))
# print(x)
#// Accessing list elements
# print(x[-2])
#// Changing list elements
# x[1] = "world"
# print(x)
#// Adding list elements
# x.append("world")
# x.insert(1, "world")
# y = [2,3,4]
# x.extend(y)
# print(x)

#// Removing list items
# x.pop()
# x.pop(1)
# x.remove("hello")
# print(x)


#? tuples
#// ordered, indexed, immutable, allows duplicates
# myTuple = (1,"hello",2.5)
# # print(myTuple)
# #// Changing tuple elements
# tupleList = list(myTuple)
# tupleList[1] = "World"
# myTuple = tuple(tupleList)
# print(myTuple)


#? sets
#// unordered, unindexed, *immutabale, no duplicates
mySet = {1, "hello", 2.5}


#? dictionaries
#// *ordered, unindexed, mutable, no duplicates
thisDict = {
    "car" : "Honda",
    "year" : "2000",
    "city" : "jakarta"
}
# print(thisDict)
#// Accessing dictionary elements
# print(thisDict["car"])
# print(thisDict["year"])
# print(thisDict["city"])

#// Changing dictionary elements
# thisDict["car"] = "Toyota"
# thisDict.update({"year": "2010"})
# print(thisDict)

#// Adding dictionary elements
# thisDict["color"] = "yellow"
# print(thisDict)

# #// Removing dictionary elements
# thisDict.pop("color")
# print(thisDict)

# ? for loop
# for i in x:
#     print(i)


# ? while loop
index = 0
while index <= 2:
    print(x[index])
    index += 1