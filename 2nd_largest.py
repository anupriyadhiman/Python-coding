#For any given integer array A (read as input by the user), How will you find the second larget element/value in the array ?
# Write a python program to solve this problem.
list = []
largest = 0
second_largest = 0
print("Enter number of elements in the required array :")
n = int(input())
for i in range(n):
    list1 = int(input())
    list.append(list1)
print(list)
for i in range(0, len(list)):
    if largest < list[i]:
        second_largest = largest
        largest = list[i]
    elif second_largest < list[i] and list[i] < largest:
        second_largest=list[i]
print(second_largest)