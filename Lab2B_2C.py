#Lab 2B
x = 545
bin(x)
y = 24
bin(y)
print "Values before modification: x: {} and y: {}".format(x, y)
x = int(0b1010100001)
y = int(0b01000)
print "Values after modification: x: {} and y: {}".format(x, y)
answer1 = int(x + y)
answer2 = int(x - y)
answer3 = int(x * y)
answer4 = int(x / 4)
answer5 = int(x % 3)
answer6 = int(y**2)
print "1: {}\n2: {}\n3: {}\n4: {}\n5: {}\n6: {}\n\b===================================".format(answer1, answer2,answer3, answer4, answer5, answer6)
