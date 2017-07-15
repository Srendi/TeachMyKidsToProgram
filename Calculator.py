# Author: Lily and Dad
# Date: 15 July 2017
# Description: A simple arithmatic calculator
# Purpose: To demonstrate input, output and conditional decision making
# Todo: Add more operators

def main():
	varA = input("Please enter a number: ")
	varB = input("Please enter a another number: ")
	varOperator = raw_input("please enter an operator (+,-,*,/): ")
	print("You entered " + str(varOperator))
	if str(varOperator) == "+":
		resultNum = str(varA+varB)
	elif str(varOperator) == "*":
		resultNum = str(varA*varB)
	elif str(varOperator) == "-":
		resultNum = str(varA-varB)
	elif str(varOperator) == "/":
		resultNum = str(varA/varB)
	else:
		print("Unknown operator try plus, minus, multiplication, or division")
	print(str(varA) + " " + str(varOperator) + " " + str(varB) + " = " + str(resultNum))

if __name__ == "__main__":
	main()
