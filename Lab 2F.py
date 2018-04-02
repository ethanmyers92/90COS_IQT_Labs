#Lab 2F
#"Write a program that will be able to check if two words (strings) are anagrams."
print "Enter your words to see if they are anagrams!"
string1 = raw_input("Enter a word: ")
string2 = raw_input("Enter a word: ")
string1a = string1.replace(" ", "")
string2a = string2.replace(" ", "")
string1b = string1a.upper()
string2b = string2a.upper()
print sorted(string1b)
print sorted(string2b)
anagram_or_not = (sorted(string1b) == sorted(string2b))
print anagram_or_not

if anagram_or_not==True:
        print "You entered anagrams!"
else:
        print "Your words are NOT anagrams!"
        





