from math import pi

input_radians = int(input("Enter radian angle: "))

answer_degree = input_radians * (180 / pi)
rounded_answer = round(answer_degree, 3)

print(f'{input_radians} rad is {rounded_answer}\N{DEGREE SIGN}')