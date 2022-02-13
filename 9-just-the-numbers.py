initial_list = [-3, 24, -6, 16, 12, 3, 29, 30, -8, 2]

for i in initial_list:
    # remove number that are negative
    if (i < 0):
        initial_list.remove(i)

print(initial_list)