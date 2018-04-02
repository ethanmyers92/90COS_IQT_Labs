#Lab 3A

mad_libs = {'adjective' : raw_input("Enter an adjective: ")}
mad_libs['nationality'] = raw_input("Enter a nationality: ")
mad_libs['person'] = raw_input("Enter a person's name: ")
mad_libs['noun1'] = raw_input("Enter a noun: ")
mad_libs['noun2'] = raw_input("Enter a noun: ")
mad_libs['adjective2'] = raw_input("Enter an adjective: ")
mad_libs['adjective3'] = raw_input("Enter an adjective: ")
mad_libs['adjective4'] = raw_input("Enter an adjective: ")
mad_libs['plural1'] = raw_input("Enter a plural noun: ")
mad_libs['noun3'] = raw_input("Enter a noun: ")
mad_libs['number1'] = raw_input("Enter a number: ")
mad_libs['shape'] = raw_input("Enter a shape: ")
mad_libs['food1'] = raw_input("Enter a food: ")
mad_libs['food2'] = raw_input("Enter a food: ")
mad_libs['number2'] = raw_input("Enter a number: ")
print ""
print "Pizza was invented by a(n) {adjective} {nationality} chef named {person}. To make a pizza, you need to take a lump of {noun1}, and make a thin, round, \
{adjective2} {noun2}. Then you cover it with {adjective3} sauce, {adjective4} cheese, and fresh chopped {plural1}. Next you have to bake it in a very hot {noun3}. \
When it is done, cut it into {number1} {shape}s. Some kids like {food1} pizza the best, but my favorite is the {food2} pizza. If I could, I would eat pizza {number2} \
times a day!".format(**mad_libs)
