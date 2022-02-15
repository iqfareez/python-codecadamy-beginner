input_string = input("Please enter text: ")

text = list(input_string)

new_text = ""

for char in text:
    new_text += char * 2

print(new_text)
