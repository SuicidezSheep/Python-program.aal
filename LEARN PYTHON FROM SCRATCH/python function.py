#obtain BMI

print("BMI")
height = float(input("Enter height: "))
weight = float(input("Enter weight: "))

height_meter = height * 0.3048
bmi = weight / (height_meter * height_meter)
print("Your bmi is: ",bmi)



#book library
book_stock = 100
result = 0
updated_stock = 0
#book library
def main():
    print("Current book stock: ", book_stock )
    while True:
        print("1. Add Stock\n2. Sell book\n3. Show Statistic\n4. Exit\n")
        option = int(input("Enter option: "))

        if option == 1:
            add_quantity = int(input("Enter quantity of books to add: "))
            updated_stock = add_stock_func(book_stock, add_quantity)
            print("Updated quantity: ", updated_stock)
        elif option == 2:
            sell_quantity = int(input("Enter quantity of books to sell: "))
            updated_stock = sell_book_func(book_stock, sell_quantity)
            print("Current stock: ",updated_stock)
        elif option == 3:
            statistic = show_statistic_func(book_stock)
            print("Library statistic: ", updated_stock)
        elif option == 4:
            break

        print("Updated book stock: ",updated_stock)


#arithmetic calculator
def add_stock_func(book_stock, add_quantity):
    result = book_stock + add_quantity
    return result

def sell_book_func(book_stock, sell_quantity):
    result = book_stock - sell_quantity
    return result
    
def show_statistic_func():
    return result

def exit_func():
    return result

main()

#arithmetic calculator
def main():
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")

    operator = int(input("Enter operator: "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operator == 1:
        result = addFunc(num1, num2)
        print(result)
    elif operator == 2:
        result = diffFunc(num1, num2)
        print(result)
    elif operator == 3:
        result = multFunc(num1, num2)
        print(result)
    elif operator == 4:
        result = diviFunc(num1, num2)
        print(result)
        

def addFunc(num1, num2):
    result = num1 + num2
    return result

def diffFunc(num1, num2):
    result = num1 - num2
    return result

def multFunc(num1, num2):
    result = num1 * num2
    return result

def diviFunc(num1, num2):
    result = num1 / num2
    return result

main()