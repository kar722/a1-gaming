# creating an empty list
list = []

n = int(input("Enter number of elements: "))
print("Enter your numbers here: ")

# iterating till the range
for i in range(0, n):
    ele = int(input())

    list.append(ele) # adding the element

list.sort()
print(list)