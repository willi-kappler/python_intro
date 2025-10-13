Repeating stuff in Python
=========================

For Loops
---------

Now what would you do if you want to print out every value in an array? From what you know until now you might
think of using the first options shown here, but this would be a very time-consuming option. Using a for loop, as
shown for the second option here will allow you to print individal values that match a condition, or do an calcualtion
with this value.

.. code-block:: python

    # using for loops to iterate through lists and arrays
    a = ([1, 2, 3, 4])
    # Option 1 for printing out every single value
    print(a[0])
    print(a[1])
    print(a[2])
    print(a[3])

    # In this example, the result will look like:
    # 1
    # 2
    # 3
    # 4

    # Option 2 for printing out values individually
    for i in range(0, len(a), 1):
        print(f"index: {i}, value{a[i]}")

    # In this example, the result will look like:
    # index: 0, value1
    # index: 1, value2
    # index: 2, value3
    # index: 3, value4

A loop is used to iteratie over a sequence, which could consist of a list, tuple, dictionary etc. Using a for loop you
can access every elemnt in a list or every letter in a word one by one using this command:

.. code-block:: python

    name = "Python"
    # Now iterate over each character in the string:

    for c in name:
        print(c)

    # The output is:
    # P
    # y
    # t
    # h
    # o
    # n


As you can see the syntax here includes a colon after the condition of the iteration. The next line is then indented.
All the lines which you want to execute during one iteration have to be indented.

.. code-block:: python

    antarctic_research_stations = ["Halley", "Neumayer", "Rothera", "McMurdo", "Amundsen-Scott South Pole", "Concordia", "Casey", "etc."]
    for station in antarctic_research_stations:
        print(station)

While Loops
-----------

As long as the condition is true, in this case the x is smaller than 10, the while loop can execute a set of statements,
such as pringing the value. A while loop is useful when trying to repaet a specific calculation on unknown numbers
until certain condition is met. An example for this might be the input of a password in a code. As long
as the password is not correct, the code will return "Sorry this password is incorrect!. Once the right password was
entered the while loop will terminate and the code can continue.
Difference to a for loop: A for loop always has an ending, while the while loop could run endlessly (which might
cause problems: your program will never finish until you kill it).

.. code-block:: python

    x = 0
    while x < 10:
        x = x + 1
        print(f"x: {x}")

To exit the while loop use the ``break`` keyword.

.. code-block:: python

    x = 0
    while x < 10:
        x = x + 1
        print(f"x: {x}")
        if x > 9:
            break

In this example, the while loop will be terminated once x is greater than 9. If this ``break`` keyword in combination
with the if condition would not be included here, then this would be an endless loop and the porgram would never terminate.
