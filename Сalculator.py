# цикл працює до поки number_1 не буде = int, input буде повторюватись
while True:
    number_1 = input("Please enter the first number:\n")
    # перевірка на число, повертає тру якщо всі символи це цифри
    if number_1.isdigit():
        num_1 = int(number_1)
        # перевірка чи є 0 у перемінній
        if num_1 != 0:
            break
        else:
            print("Error. Number is zero!")
    else:
        print("Please enter a number!")

while True:
    number_2 = input("Please enter the second number:\n")

    if number_2.isdigit():
        num_2 = int(number_2)
        if num_2 != 0:
            break
        else:
            print("Error. Number is zero!")
        break

    else:
        print("Please enter a number!")

while True:
    operator = input("Select an operator: \n1 '+' \n2 '-' \n3 '*' \n4 '/'\n")

    if operator == "1":
        result = int(number_1) + int(number_2)
        break

    elif operator == "2":
        result = int(number_1) - int(number_2)
        break

    elif operator == "3":
        result = int(number_1) * int(number_2)
        break

    elif operator == "4":
        result = int(number_1) / int(number_2)
        break

    else:
        if operator != "1" "2" "3" "4":
            print("please enter operator!")

print(result)
