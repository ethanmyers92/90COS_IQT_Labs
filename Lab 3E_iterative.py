print "Iterative function, returns first 100 Fibonacci Numbers: "
def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

count = 0
while count <= 100:
	print fibi(count)
	count += 1
else:
	print "DONE!"
count
