# Just a Simple CLI Factorial Program Using While Loop.

# __main__
print('Program to Know Factorial of a Number ♥')
num=int(input('♥ Enter the Number:'))
fact=1

if (num== 0) or (num == 1) :
    print(f'The Factorial of {num} is 1')
elif(num>1):
    printfNum=num
    while num>0:
        fact=fact*num
        num-=1
    print(f'The factorial of {printfNum} is {fact}.')
else:
    print('The Entered number is negative or Invalid Bruh ♥')