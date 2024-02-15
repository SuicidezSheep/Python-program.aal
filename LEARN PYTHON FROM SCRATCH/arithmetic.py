while True:
  num1 = float(input("Enter First Number:"))
  num2 = float(input("Enter Second Number:"))
  op = input("Enter an Operator:")

  if op == '+':
      print(num1,"+",num2,"=",num1 + num2)
  if op == '-':
      print(num1,"+",num2,"=",num1 - num2)
  if op == '*':
      print(num1,"+",num2,"=",num1 * num2)
  if op == '/':
      print(num1,"+",num2,"=",num1 / num2)
  ask = input("Want to Stop? (stop):")
  if ask == "stop":
         break