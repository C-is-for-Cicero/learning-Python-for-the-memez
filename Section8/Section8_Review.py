def maker_function(user_input_string):
    capitalised = str.capitalize(user_input_string)
    first_word = capitalised.split()[0]
    if first_word == "How" or first_word == "Why" or first_word == "When" or first_word == "What" or first_word == "Where":
        result = capitalised+'?'
    else:
        result = capitalised+'.'
    return result

list_1 =[]

while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        list_1.append(maker_function(user_input))

print(list_1)




