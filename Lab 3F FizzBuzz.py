for i in xrange(1, 100):
    if i % 3 == 0:
        if i % 5 == 0:
            print "FizzBuzz".format(i)
        else:
    	    print "Buzz".format(i)
    	    continue
        
    if i % 5 == 0:
        if i % 3 == 0:
            continue
        else:
            print "Fizz".format(i)
            continue
    print str(i).format(i)
