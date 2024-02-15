

print("\n\n\n")
print("Menu\n"
      "1. burger = 10\n"
      "2. pizza = 20\n"
      "3. fries = 30\n"
      )
price: float;
my_order = int(input("Enter your order: "))

if my_order == 1:
      print("burger = 10")
      payment_amount = float(input("Enter payment amount: "))
      if payment_amount < 10:
              print("Insufficient balance!\n")
      elif payment_amount >= 10:
              change: float;
              change = payment_amount - 10 
              print("Successful Transaction!")
              print("balance: ", change)
      else:
              print("invalid Entry!\n")

elif my_order == 2:
      print("pizza = 20")
      payment_amount = float(input("Enter payment amount: "))
      if payment_amount < 20:
              print("Insufficient balance!\n")
      elif payment_amount >= 20:
              change: float;
              change = payment_amount - 20
              print("Successful Transaction!")
              print("balance: ", change)
      else:
              print("invalid Entry!\n")
elif my_order == 3:
      print("fries = 30")
      payment_amount = float(input("Enter payment amount: "))
      if payment_amount < 30:
              print("Insufficient balance!\n")
      elif payment_amount >= 30:
              change: float;
              change = payment_amount - 30
              print("Successful Transaction!")
              print("balance: ", change)
      else:
              print("invalid Entry!\n")
else:
      print("Invalid Entry!\n")




print("Person 1")
my_name = str(input("Enter name: "))
my_age = int(input("Enter age: "))
my_address = str(input("Enter address: "))
print("")

print("Name: ", my_name)
print("Age: ", my_age)
print("Address: ", my_address)

print("\n")

print("Person 2")
my_name2 = str(input("Enter name: "))
my_age2 = int(input("Enter age: "))
my_address2 = str(input("Enter address: "))
print("")

print("Name: ", my_name2)
print("Age: ", my_age2)
print("Address: ", my_address2)

print("")

older = my_age >= my_age2
print(older, my_age, ">=", my_age2)
print('\n\n\n')

firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

print("\nChoose operation\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Division\n")

operator = int(input("Chooose operator: "))
output: int;
if operator == 1:
                output = firstNum + secondNum
                print(firstNum,"+",secondNum,"=", output)
elif operator == 2:
                output = firstNum - secondNum
                print(firstNum,"-",secondNum,"=", output)
elif operator == 3:
                output = firstNum * secondNum
                print(firstNum,"*",secondNum,"=", output)
elif operator == 4:
                output = firstNum / secondNum
                print(firstNum,"/",secondNum,"=", output)           
else:
                print("Invalid Entry!\n")     
print('\n\n\n')


x = 5
y = 10

result = x > y #boolean FALSE, x is not greater than y
print("X is less than Y",result)

result = y > x #boolean TRUE, y is greater than  x
print("Y is greater than X", result)

print("Hello, World!")          