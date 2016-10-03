
# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def tax_calculation(cost, state, tax=0.05):
    """
    Calculates total cost.

    Calculates the cost of an item with tax rate applied. Tax rate defaults to 5 percent unless the input state is California, in which case 7 percent is applied, or unless a different tax rate is specified. The input string for 'state' is shifted to uppercase for accuracy in equality evaluation.

    For example:
        >>> tax_calculation(100, "ca")
        107.0
        >>> tax_calculation(100, "va")
        105.0
        >>> tax_calculation(100, "va", 0.1)
        110.0
    """
    ## JB: I want to find a way to override the 7% tax rate if the state *IS*
    # California, but have not been able to yet, because "is not tax" won't
    # evaluate as true when a default value is specified in the function.
    if state.upper() == "CA":
        return cost + cost * 0.07
    else:
        return cost + cost * tax


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".


def is_berry(fruit):
    """
    Evaluates if input is a berry.

    Takes an input string and evaluates whether or not it is a member of the predefined 'VALID_FRUITS' list. Returns True if yes, False if no. The input string for 'fruit' is shifted to lowercase for accuracy in equality evaluation.

    For example:
        >>> is_berry("strawberry")
        True
        >>> is_berry("CHERRY")
        True
        >>> is_berry("apple")
        False
    """
    VALID_FRUITS = ["strawberry", "cherry", "blackberry"]
    if fruit.lower() in VALID_FRUITS:
        return True
    else:
        return False

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit):
    """
    Calculates shipping cost for fruit type.

    Takes an input string and calculates its shipping cost. Calls the external function is_berry() on its own input to determine if input fruit is or is not a berry. Shipping cost is conditional based on whether or not the fruit input is a berry.

    For example:
        >>> shipping_cost("cherry")
        0
        >>> shipping_cost("BLACKBERRY")
        0
        >>> shipping_cost("APPLE")
        5
        >>> shipping_cost("kittens")
        5
    """
    if is_berry(fruit) is True:
        return 0
    else:
        return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.


def is_hometown(townname):
    """
    Evaluates if input is my hometown.

    Takes an input string and evaluates whether or not it is the same as the author's hometown. Returns True if yes, False if no. The input string for 'townname' is shifted to lowercase for accuracy in equality evaluation.

    For example:
        >>> is_hometown("livermore")
        True
        >>> is_hometown("oakland")
        False
        >>> is_hometown("new york")
        False
        >>> is_hometown("SAN FRANCISCO")
        False
    """
    if townname.lower() == "livermore":
        return True
    else:
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first, last):
    """
    Concatenates two name values into a single string.

    Takes two input strings and concatenates them into a single string, separated by a space. Does not adjust upper/lowercase.

    For example:
        >>> full_name("Jen", "Brabec")
        'Jen Brabec'
        >>> full_name("Kitty", "McKittersons")
        'Kitty McKittersons'
        >>> full_name("LITTLE", "kitty")
        'LITTLE kitty'
    """
    ## JB comment: I want to allow for last name to be omitted (via last=""
    ## default value above), but how to construct an if/then statement to also
    ## omit the space (" ") in string concatenation in return statement?
    ## If last name has a default then "is not last" will not evaluate as True.
    return first + " " + last

#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(townname, first, last):
    """
    Constructs a greeting statement.

    Takes an input list and concatenates the items into a greeting statement. Calls the external functions hometown() on the first input list element, and full_name() on the second and third elements. Evaluates if input townname is the same as the author's hometown. Uses full_name() to create one string out of the two passed name values (first, last). Unifies these two results into one of two possible greetings, depending on whether or not is_hometown() evaluates as true.

    For example:
        >>> hometown_greeting("livermore", "parker", "kitty")
        Hi, parker kitty, we're from the same place!
        >>> hometown_greeting("princeton", "Mike", "Boyfriend")
        Hi, Mike Boyfriend, where are you from?
    """
    if is_hometown(townname) is True:
        print "Hi, " + full_name(first, last) + ", we're from the same place!"
    else:
        print "Hi, " + full_name(first, last) + ", where are you from?"


#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def increment(x=1):
    """
    Increments the passed argument.

    Takes an integer and passes it to the nested add() function. add() returns the sum of its argument and the first argument. increment() returns the result of add().

    For example:
        >>> addfive = increment(5)
        >>> addfive(5)
        10
        >>> addfive(20)
        25
    """
    def add(y):
        return x + y
    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
addfive(5)
addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def add_num_to_list(number, numberlist):
    """
    Adds a number to the end of a list.

    Takes a number as its first argument and adds it to the end of the list in its second argument.

    For example:
        >>> add_num_to_list(5, [1, 2, 3, 4])
        [1, 2, 3, 4, 5]
        >>> somenum = 6
        >>> somelist = [2, 3, 1, 5, 4]
        >>> add_num_to_list(somenum, somelist)
        [2, 3, 1, 5, 4, 6]
    """
    numberlist.append(number)
    return numberlist

#####################################################################

#####################################################################
## tests for DocStrings passing

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
