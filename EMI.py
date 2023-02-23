print("Enter the amount that you want to calculate EMI on :")
p = float(input())
print("Enter the rate at which the loan is taken :")
R = float(input())
r=R/12/100
print("Enter the number of months:")
n = float(input())

EMI = (p*r*((1+r)**n))/((1+r)**n-1)

print(EMI)