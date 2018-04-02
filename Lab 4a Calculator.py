#Lab 4a Calculator

add = lambda x,y: x + y
subtract = lambda x,y: x - y
multipy = lambda x,y: x * y
divide = lambda x,y: x / y
power = lambda x,y: x ** y

print "Welcome to the Python Calculator!"
print "1. Add"
print "2. Subtract"
print "3. Multipy"
print "4. Divide"
print "5. Power (Exponent)"

# Take input from the user
choice = str(input("Enter choice(1/2/3/4/5):"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,'+',num2,'=',add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   print(num1,"**",num2,"=", power(num1,num2))

else:
   print("Invalid input")
