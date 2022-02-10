def is_x_equal_o(text: str):
    # make text lower case for easy comparison
    text_lower = text.lower()

    # counts the numer of Os and Xs
    o_counts = text_lower.count("o")
    x_counts = text_lower.count("x")

    # print(f"O count is {o_counts}")
    # print(f"X count is {x_counts}")

    return x_counts == o_counts  # return bool


input_text = input("Please enter text: ")
print(is_x_equal_o(input_text))
