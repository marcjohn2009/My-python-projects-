print("Welcome to marc john's python project")

print("[1] Calculator")

print("[2] Multiplication Table")

math = input("What do you want to do (1, 2) : ")

if math == "2":
	shesh = int(input("Please enter a number: "))
	
	for i in range(1, 10):
		print(shesh, "x", i, "=", shesh * i)
		
elif math == "1":
	print("[1] Addition (+)")
	print("[2] Substraction (-)")
	print("[3] Division (÷)")
	print("[4] Multiplication (x)")
	
	operator = input("Enter an operator(1 2 3 4): ")
	
	if operator == "1":
		num1 = int(input("Enter your first number: "))
		num2 = int(input("Enter your 2nd number: "))
		
		print(num1, "+", num2, "=", num1 + num2)
		
	elif operator == "2":
		num1 = int(input("Enter your first number: "))
		num2 = int(input("Enter your 2nd number: "))
		
		print(num1, "-", num2, "=", num1 - num2)
		
	elif operator == "3":
		num1 = int(input("Enter your first number: "))
		num2 = int(input("Enter your 2nd number: "))
		
		print(num1, "÷", num2, "=", num1 / num2)
		
	elif operator == "4":
		num1 = int(input("Enter your first number: "))
		num2 = int(input("Enter your 2nd number: "))
		
		print(num1, "x", num2, "=", num1 * num2)
		
	else:
		print("Invalid input.")
		
	
else:
	print("Invalid Input.")
