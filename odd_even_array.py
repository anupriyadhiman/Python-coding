#Given an array nums (read as input by the user), separate the odd and even numbers from the array and print them on separate lines.
list = []
oddlist = []
evenlist = []
temp = 0
print("Enter number of elements in the required array :")
n = int(input())
for i in range(n):
    list1 = int(input())
    list.append(list1)
print(list)
for i in range(0,n):
    temp = list[i]
    if temp%2 == 0:
        oddlist.append(temp)
    else:
        evenlist.append(temp)
print(oddlist)
print(evenlist)
