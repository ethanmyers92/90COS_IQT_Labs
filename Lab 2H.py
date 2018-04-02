#Lab 2H

print "Enter the grades for your four students into your gradebook! Enter grade first then name!"
student_dict = {raw_input("Enter first student's name: ") : int(raw_input("Enter first student's grade: "))}
student_dict[raw_input("Enter second student's name: ")] = int(raw_input("Enter second student's grade: "))
student_dict[raw_input("Enter third student's name: ")] = int(raw_input("Enter third student's grade: "))
student_dict[raw_input("Enter fourth student's name: ")] = int(raw_input("Enter fourth student's grade: "))

print student_dict
print ""
print "Grades, High to low: "
print sorted(student_dict.items(), key=lambda x:x[1], reverse=True)
print ""
print "The average grade is : "
class_average = sum(student_dict.values()) / len(student_dict.values())
print class_average

#NOTES:
#for key, value in sorted(student_dict.items()):
#	print key, value
#print sorted(student_dict.values()
#print sorted(student_dict, key=student_dict.get, reverse=True)
#To get a list of tuples ordered by value
#Print sorted(student_dict.items(), key=lambda x:x[1])
#student_dict = {"Alice" : 99, "Thomas" : 67, "Betty" : 75, "Dexter" : 83}
