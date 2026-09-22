#camel case to snake case(used aai)
#camel case exa=firstName
#snake_case exa=first_name
#1 ask user for input
#2 the input should be in camel case
#3 replace "" with "_" and replace the capital letter with small letter


user_input=input("camelCase:")
new_string=""
for letter in user_input:
    if letter.isupper():
       new_string+="_"+letter.lower()
    else:
        new_string+=letter.lower()

print("snake_case:",new_string)

