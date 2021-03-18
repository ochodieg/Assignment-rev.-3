import equation_parts

# function prompts user to continue
def continue_loop() -> bool:
    """Asks user if they would like to continue."""
    validated = True
    while validated:
        question = input("\n" +
        "Would you like to enter another equation? (Y)es or (N)o.\n")
        val_in = question.lower()
        # validates input by converting whatever is typed into lower case.
        if val_in == "y" or val_in == "yes":
            choice = True
            validated = False
        elif val_in == "n" or val_in == "no":
            choice = False
            validated = False
        else:
            print("I did not understand your choice.")
    return choice

# This is the while loop that runs script
validated = True
while validated:

    equation = input("Special rules:\n\t'*' is forbidden\n\t'\\' "\
    "is used for integer division.\n\t'%' is used for modulus division." +
    "\nEnter a basic math equation.\n\t\t")

    # these three variabel store a list of character that will be referenced
    # to determine parts of the equation
    numbers = "1234567890"
    deci = "."
    good_ops = "+-xX/\\%"

    # these variables initialize an empty string that will be concatenated to
    first_op = ""
    second_op = ""
    operator = ""

    ignore = " "

    ndx = 0


    while ndx < len(equation):
        if equation[ndx] in numbers or equation[ndx] in deci:
    # this while loop iterates by index in "equation" variable
    # uses the "in" function to check whether a string character
    # is found in that list. It will iterate until it gets to
    # a character value that is not on the list
            first_half = equation[0:ndx+1]
            sub_string = equation[ndx+1:99]
            ndx += 1
    # until the loop stops, it will add all the characters in the
    # first operator to the first_op variable and then create a
    # new variable with all of the characters NOT in the first_op
    # variable. Recall that strings are immutable and hence, original string
    # cant be modified. This is why I had to use a while loop for this bit
    # as a for loop would iterate through all characters and add values found
    # in the "numbers" variable to the first operand
        elif equation[ndx] in ignore:
            ndx += 1
        elif equation[ndx] not in numbers:
            ndx = len(equation)
    # Because I am using a while loop on the first part to
    # seperate operands, space values will be concatenated to
    # operands. This for loop strips those space values.
    for chr in first_half:
        if chr in numbers or chr in deci:
            first_op += chr


    # Now that we don't have to seperate numbers
    # from two operands we can use for loops to find
    # the operator. This will also strip space values
    for chr in sub_string:
        if chr in good_ops:
            operator += chr


    # this for loops takes the new string created by while loop and
    # strips off spaces and operators to give only the remaining
    # operator
    for chr in sub_string:
        if chr in numbers or chr in deci:
            second_op += chr


    answer = equation_parts.get_math_answer(operator,first_op,second_op)
    # if statement was made to give explanation for 0.0 output when "*"
    # operator is being used as it is not allowed as per assignment requirement
    if answer == 0.0000:
        answer = str(answer) +\
                 "\nIf the answer is wrong, " \
                 "make sure not to use the forbidden operator."
        print("\n{} {} {} = {}\n"
              "The result is "
              "{}".format(first_op, operator, second_op, 0.0 ,answer))
        validated = continue_loop()
    else:
        answer = answer
        print("{} {} {} = {}\n"
              "The answer to this equation "
              "is {}".format(first_op, operator, second_op, answer,answer))
        validated = continue_loop()
