# This function is able to return a variable that represents the elements of an input list being "joined" together to
# form an integer. Since the output is required to be in an integer form, and that we are not allowed to perform any
# type conversion, my approach is to join the elements by adding them to each other while considering the amount of
# digits they have. We can't simply add numbers together, as adding 1 and 3 won't result into 13. So what we do is,
# we "add zeroes" to the current output number by the amount of digits that the next element in the list (that we
# want to join) has. So that way, 1 and 3 becomes 10 and 3, which results into the 13 that we want! The same goes for
# 20 and 30, as 20 becomes 2000 ( as 30 has two digits, so we add two zeroes behind 20 ) and we add them to become
# 2030, the result we desire.

def element_printer(input_list):
    """
    :param input_list: This is the variable that signifies the input list, we will be accessing
    elements from this list.
    :return: output: An integer that will contain the number which contains the elements of the lists being "joined"
    together.
    """
    if len(input_list) == 0:            # If the List is empty, then just return None
        return None
    output = 0                          # The final output variable that we want to return, is initialised here

    for i in range(len(input_list)):    # We use a for loop to iterate through every element in the input_list.
        element = input_list[i]         # Retrieve the current element/number that we want to join to the output.
        if i != 0:                      # Skip this step for the first iteration, since the addition at the end
                                        # of the loop will always represent the correct number for the first one.
            digit = 0                   # Initialize a variable that will be used to count element's digits.

            while element != 0:         # While element is not 0, keep dividing it by 10, while adding digit by 1
                element //= 10          # each time.
                digit += 1

            if digit == 0:              # Since our earlier while loop won't run if the element is 0, we still need to
                digit += 1              # set the amount of digit to 1, since we need at least 1 digit to represent 0.
                                        # If we do not set the digit to 1, 0 won't be joined in our output number.
            output *= (10 ** digit)     # Multiply the current output by the amount of digits in the current element.

        output += input_list[i]         # After "adding enough zeroes to the back of the number", only then can we
                                        # add the current element

    return output                       # Return the final output.


# Working Example:
# List = [20, 3]
# output_number = 0
# 1st iteration:
# output_number = 0 + 20 = 20
# 2nd iteration:
# 3 has 1 digit, so we multiply output_number by 10
# output_number = 20 * 10 = 200
# output_number = 200 + 3 = 203

# Working Example 2:
# List = [1, 204]
# 1st iteration:
# output_number = 0 + 1 = 1
# 2nd iteration:
# 204 has 3 digits, so we multiply output_number by 10 ^ 3 = 1000
# output_number = 1 * 1000 = 1000
# output_number = 1000 + 204 = 1204
if __name__ == '__main__':
    print(element_printer([1, 2, 3, 4]))
    print(element_printer([1]))
    print(element_printer([1, 12, 13, 12]))
    print(element_printer([100, 2, 6789]))
    print(element_printer([0, 20, 4]))
    print(element_printer([1, 0]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
