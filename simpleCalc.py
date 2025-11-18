#Just a CLI Calc made while Listening 🎵🎵

# __main__

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
op=input("Enter: \n + to add. \n - to subtract. \n * to Multiply. \n \\ to Divide.")

if (op == '+'):
    print('The sum is:', a+b)
elif (op == '-'):
    print('The subtraction is', a-b)
elif (op == '*'):
    print('The multiplication is', a*b)
elif (op == '/'):
    print('The division is:', a/b)
else:
    print('Invalid Input')
