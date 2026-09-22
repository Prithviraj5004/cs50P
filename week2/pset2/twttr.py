#1 ask user for input(almost got it not in given by mummy)
#2 remove vowels from the string a,e,i,o,u
#3 display the remaining string


user_input=input("Enter tweet:")
new_string=""
for letter in user_input:
    if letter.lower() not in ["a","e","i","o","u"]:
        new_string+=letter




print(new_string)
