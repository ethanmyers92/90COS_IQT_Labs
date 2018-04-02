for i in xrange(1, 100):
    if i % 15 == 0:
        print "FizzBuzz".format(i)
        continue #prevents second print from running
    if i % 3 == 0:
        print "Fizz".format(i)
        continue
    if i % 5 == 0:
        print "Buzz".format(i)
        continue
    print str(i).format(i)
