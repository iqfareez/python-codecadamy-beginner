text_input = input("Please enter a word: ")

# make all character sequence in lower case
characters_from_text = list(text_input.lower())

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for vowel in vowels:
    # count if found the vowels in input character set
    count += text_input.count(vowel)

print(f"Total nnumber of vowels in {text_input} is {count}")
