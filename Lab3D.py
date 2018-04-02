#Lab3D
#Write a program that prompts a user to input an integer and calculates the factorial of that number using a while loop.

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

count = 0
while count <= 100:
	print factorial(count)
	count += 1
else:
	print "DONE!"	

#print factorial(int(raw_input("Enter a number you would like the factorial of: ")))
