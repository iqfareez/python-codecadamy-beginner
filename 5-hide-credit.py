input_credit_card = input("Please enter your credit card number 🔪: ")

# extract without the last 4 digits and combine them with '*'
result = input_credit_card[:-4] + "****"

print(result)
