dec_input = int(input("Please enter integer digit: "))

# using built-in decimal to binary converter 😎
bin_number = bin(dec_input)
print(bin_number.replace("0b", ""))
