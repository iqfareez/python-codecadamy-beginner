import random


def sortNumbers(nums: list, sortingMode: str) -> list:

    #  we can do using this two line of code, 
    #  but if we pass anything other than none/desc/asc,
    #  it will not detect an error
    #
    # if (sortingMode == "none"): return nums
    # return sorted(nums, reverse=sortingMode == "desc")

    # compare the sortingMode parameter
    # and do the necessary operation
    match sortingMode:
        case "none":
            return nums
        case "asc":
            return sorted(nums)
        case "desc": 
            return sorted(nums, reverse=True)
        case _:
            # raise error if value passed other than asc/desc/none
            raise ValueError("Sorting mode only asc/desc/none")


# generate 30 random number
numbers = random.sample(range(0, 30), 30)

# print original list of numbers
print("Original list of numbers:")
print(numbers)

# define sorting mode
# and print the answer
sortingMode = "asc" # can change to asc/desc/none
sortedNumbers = sortNumbers(numbers, sortingMode)

print(f"\nSorting Mode: {sortingMode}: ")
print(sortedNumbers)
 