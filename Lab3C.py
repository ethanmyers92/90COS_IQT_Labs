#Lab3C: The 'Fun House'
print "Welcome to Fun House! Choose door 1, 2, or 3..."

input = raw_input()

if input == "1":
    #<code>
    print"Welcome to Room 1! You have the chance \
    to win one million dollars! Pick a number between 1 and 10!"
    input2 = raw_input()
    if input2 == "7":
    	print "It's your lucky day! You've won a million dollars and \
    	you can continue through the house.. Pick 1 to continue into the \
    	basement, or pick another number to leave the Fun House"
    	input3 = raw_input()
    	if input3 == "1":
    		print "Congrats! You've completed Room 1 of the Fun House!"
    	else:
    		print "Good riddance!"	
    else:
    	print "You chose incorrectly! Game Over!"

elif input == "2":
    print "Welcome to Room 2! Not much to see here. Start over and check out \
    Room 1!"

elif input == "3":
    print "Welcome to Room 3! Not much to see here. Start over and check out \
    Room 1!"
else:
    print "... Follow directions please."
