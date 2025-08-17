print("Program to check factorial of a number.")
num=int(input("Enter the number:"))
fact=1
while num>0:
    fact=num*fact
    num-=1
print("The factorial of the given number is", fact)