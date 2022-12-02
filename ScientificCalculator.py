import math

# Number Calculator
def calculation(num1, sign, num2): if sign == "+":
result = int(num1) + int(num2) print("Answer is: ", result) return result
elif sign == "-":
result = int(num1) - int(num2) print("Answer is: ", result) return result
elif sign == "x":
result = int(num1) * int(num2) print("Answer is: ", result) return result
elif sign == "/":
result = int(num1) / int(num2) print("Answer is: ", result) return result
else:
print("Invalid Input Data")

# Trigonometric Calculator
def calculation2(func, angle): if func == "sin":
x = math.degrees(angle) value = math.sin(x) print("Answer is: ", value)

elif func == "cos":
x = math.degrees(angle) value = math.cos(x) print("Answer is: ", value)

elif func == "tan":
b = math.degrees(angle) value = math.tan(b) print("Answer is: ", value)

elif func == "cosec":
b = math.degrees(angle) value = 1 / math.sin(b) print("Answer is: ", value)

elif func == "sec":
b = math.degrees(angle) value = 1 / math.cos(b)
 
print("Answer is: ", value)

elif func == "cot":
b = math.degrees(angle) value = 1 / math.tan(b) print("Answer is: ", value)

else:
print("Invalid Input Data")

def calculation3(func, angle): if func == "sin":
x = math.radians(angle) value = math.sin(x) print(value)

elif func == "cos":
b = math.radians(angle) value = math.cos(b) print(value)

elif func == "tan":
b = math.radians(angle) value = math.tan(b) print(value)

elif func == "cosec":
b = math.radians(angle) value = 1 / math.sin(b) print(value)

elif func == "sec":
b = math.radians(angle) value = 1 / math.cos(b) print(value)

elif func == "cot":
b = math.radians(angle) value = 1 / math.tan(b) print(value)

else:
print("Invalid Input Data")


while True:

z = input("You Want to open Number Calculator or Trigonometric Calculator (N/T): ")
if z == "N":
 
print(" 	
 	")





print("General Instructions: You can use Sign as ('+', '-', 'x', '/')") print("First number and Second number should be Integer")
print(" 	
 	")

a = input("What is the first number: ") b = input("What is the Sign: ")
c = input("What is second number: ") calculation(a, b, c)

elif z == "T":
print(" 	
 	")
print("General Instructions: For example- angle can be like: 'pi' or 'pi/6', etc.	")
print("You can use Trigonometric Functions like (sin, cos, tan, sec, cosec, cot)")
print("For angle in Radian type 'R' and in Degrees type 'D'	")
print(" 	
 	")

Func = input("Trigonometric Function: ") angle1 = str(input("Angle (R/D): "))


if angle1 == "R":
angle = input("what is the angle in Radians: ") calculation3(Func, angle)


elif angle1 == "D":
angle = input("What is angle in Degrees: ") calculation2(Func, angle)

else:
print("Invalid Input Data")

elif z == "quit": break

else:
print("Invalid Input Data")
