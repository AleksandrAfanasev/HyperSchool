first_number = float(input())
second_number = float(input())
arithmetic_operation = input()
if arithmetic_operation in ('div', '/', 'mod') and second_number == 0:
    print('Division by 0!')
elif arithmetic_operation == '+':
    print(first_number + second_number)
elif arithmetic_operation == '-':
    print(first_number - second_number)
elif arithmetic_operation == '/':
    print(first_number / second_number)
elif arithmetic_operation == 'mod':
    print(first_number % second_number)
elif arithmetic_operation == 'pow':
    print(first_number ** second_number)
elif arithmetic_operation == 'div':
    print(first_number // second_number)
elif arithmetic_operation == '*':
    print(first_number * second_number)
