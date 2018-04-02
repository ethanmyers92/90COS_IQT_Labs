#Lab3B
print "1. Read the entire text file"
file = open("Lab3D_GG.txt", 'r')
print file.read()
file.close()

print "-------------------------------"

print "2. Read the first 10 lines of the file: "
file = open("Lab3D_GG.txt", 'r')
lines = file.readlines()
print lines[0:9]
file.close()

print "-------------------------------"

print "3. Append text to the file and read the last 5 lines of the file: "
file = open("Lab3D_GG.txt", 'a')
file.write(" This is me appending text to the file so I can read it later!") 
file.close()
file = open("Lab3D_GG.txt", 'r')
lines = file.readlines()
print lines[-5:]
file.close()

print "-------------------------------"

print "4. Read the file line by line and store it into a list: "
file = open("Lab3D_GG.txt", 'r')
lines = file.readlines()
print lines
file.close()

print "-------------------------------"

print "5. Sort words from longest to shortest: "
file = open("Lab3D_GG.txt", 'r')
complete_string = file.read()
words = complete_string.split()
print sorted(words , key = len, reverse = True)
file.close()

print "-------------------------------"

print "6. Count the number of lines in the text file: "
num_lines = sum(1 for line in open("Lab3D_GG.txt"))
print num_lines

print "-------------------------------"

print "7. Count how many times survive is used in the text: "
total = 0

with open("Lab3D_GG.txt") as f:
    for line in f:
        found = line.find('survive')
        if found != -1 and found != 0:
            total += 1

print total

print "-------------------------------"

print "8. Copy the contents of the file to another file: "
import shutil
path = "Lab3D_GG.txt"
path2= "Lab3D_HH.txt"
shutil.copy(path, path2)
print "SEE FOLDER FOR NEW FILE NAMED 'Lab3D_HH.txt'!"
print "-------------------------------"
