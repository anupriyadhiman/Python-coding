#Given a number A (read as input ), find the sum of its digits.

from symbol import test_nocond
#Given a number A (read as input ), find the sum of its digits.
n = int(input("Enter a number :"))
sum = 0
while(n != 0):
    sum = sum + (n%10)
    n=int(n/10)
print(sum)


