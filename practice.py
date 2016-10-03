"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


def hello_world():
    print "Hello World"

# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


def say_hi(name):
    print "Hi " + name

# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.


def print_product(x, y):
    print x * y

# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times


def repeat_string(phrase, n):
    print phrase * n

# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".


def print_sign(integer):
    if integer > 0:
        print "Higher than 0"
    elif integer < 0:
        print "Lower than 0"
    else:
        print "Zero"

# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


def is_divisible_by_three(integer):
    # if input divided by 3 has a remainder of 0, integer is divisible by 3
    # and function returns True
    if integer % 3 == 0:
        return True
    else:
        return False

# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.


def num_spaces(sentence):
    # .count() method works on a string (the sentence argument here) and returns
    # the number of instances of whatever substring is entered between parentheses
    return sentence.count(" ")

# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


def total_meal_price(price, tip=0.15):
    # parentheses not required because order of operations rules will perform
    # (price * tip) before before (price + price)
    return price + price * tip

# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.


## JB Comments:
## I wrote a second function, pos_neg_test, to call within sign_and_parity
## in order to avoid some repetition. A single-function solution starts
## on line 193.
# this pos_neg_test function tests if an integer is less than 0
# (therfore is negative) or is greater than 0 (therefore is positive),
# corresponding to -/+ sign on integers. The sign of integer = 0 is undefined.
def pos_neg_test(integer):
        if integer < 0:
            return "Negative"
        elif integer > 0:
            return "Positive"


## JB Comments:
# as above, function examines integer input for even or odd quality.
# after odd/even is determined, the pos_neg_test function is called on the
# integer to further assign positive or negative characteristic
# results are appended to empty list 'result' in this order (parity then sign)
# and then returned at end of function
def sign_and_parity(integer):
    result = []
    if integer % 2 == 0:
        result.append("Even")
        result.append(pos_neg_test(integer))
    elif integer % 2 != 0:
        result.append("Odd")
        result.append(pos_neg_test(integer))
    return result

## JB comment: tests as per instructions on lines 147-150 are on lines 184-188
example_result = sign_and_parity(-5)

example_sign, example_parity = example_result

print example_sign, example_parity

# # JB Comments:
# # this is a more verbose way to write sign_and_parity without creating a
# #  second pos_neg_test function, which also works:
# def sign_and_parity(integer):
#     result = []
#     if integer % 2 == 0:
#         result.append("Even")
#         if integer < 0:
#             result.append("Negative")
#         elif integer > 0:
#             result.append("Positive")
#     elif integer % 2 != 0:
#         result.append("Odd")
#         if integer < 0:
#             result.append("Negative")
#         elif integer > 0:
#             result.append("Positive")
#     return result


################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.


def full_title(name, title="Engineer"):
    return title + " " + name

# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


def write_letter(name, title, sender):
    print "Dear " + full_title(name, title) + ", I think you are amazing! Sincerely, " + sender


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
