#Lab 3E
#Write one function that prints out the first 100 numbers in the Fibonacci sequence iteratively and one recursively.
#def F(n):
#   if n == 0: return 0
#    elif n == 1: return 1
#    else: return F(n-1)+F(n-2)

print "Recursive function, returns first 100 Fibonacci Numbers: "
def F(count):
    if count == 0: return 0
    elif count == 1: return 1
    else: return F(count-1)+F(count-2)
count = 0
while count <= 100:
	print F(count)
	count += 1
else:
	print "DONE!"
count

#print F(int(raw_input("Enter a number you would like to compute the Fibonacci sequence with: ")))
