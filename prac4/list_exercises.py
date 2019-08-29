# Numbers task
numbers = []
for i in range(5):
    number = int(input("Enter a Number: "))
    numbers.append(number)

print("THe first number is ", numbers[0])
print("THe last number is ", numbers[-1])
print("the smalles number is ", min(numbers))
print("the largest number is ", max(numbers))
print("the average of the numbers is ", sum(numbers) / len(numbers))

# password task
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("ENter a username: ")
if username in usernames:
    print("access granted")
else:
    print("access denied")