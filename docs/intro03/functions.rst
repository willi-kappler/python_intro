Functions in Python
====================

You already know several functions in python, such as ``print()``, ``range()``, ``len()``. Behind these words stand a block of code
which will only be executed when you call the function. Let's look at the example of the function ``len()``. When you
want to find out the length of a data structure, i.e. how many characters there are in a string, you can use the following
statement:

.. code-block:: python

    l = [1, 2, 3, 4, 5]
    print(len(l))

    # Output: 5

When using a function, you pass data, known as parameters, in this case you use the variable ``l``, into the function.
Python then runs the function and returns the results. You can find more detail about the ``len()`` function here:

https://www.w3schools.com/python/ref_func_len.asp

Why do we use or define functions? It's an abstraction method to enable re-usage of code again.

.. code-block:: python

    # Defining functions
    def add2(a, b):
        result = a + b
        return result

    def add3(a, b, c):
        return a + b + c

    s1 = add2(3, 4)
    s2 = add3(3, 4, 5)

    print(f"The sum is: {s1}")
    print(f"The sum is: {s2}")

    # How to implement this if we don't know how many values will be added:

    def add_any(values): # Use a list
        result = 0
        for v in values:
            result = result + v
        return result

    s3 = add_any([1, 1, 2, 2, 3, 3])
    s4 = add_any([])

    print(f"The sum is: {s3}")

Ask for user input
------------------

The input given is automatically saved as a string. However if you want to do any mathematical calcualtation with
this input, you either need to convert it into a float or an integer.
Why is it useful to ask the user for input? For instance, you could ask the user for the name of the file the user
whats to load. Or you could ask the user for input on the size of a sliding window for calculation
of the average. Or ask the user for input on which range of the data to plot.

.. code-block:: python

    # Ask the user for input
    name = input("What is your name? ")
    print(f"Hello {name}")

    number = input("Give me a number: ")
    number = int(number) # Convert it to an integer
    number = float(number) # Convert it to a float


.. code-block:: python

    import numpy as np
    # Ask for a file name to load:
    filename = input("Which file do you want to open? ")
    data = np.loadtxt(filename)

.. attention:: Exercise 3.2:

    Now write a function that reads in numbers from the user and calculates the total sum and prints this
    value at each iteration. The program should also print out all the numbers sorted (ascending) at the end.
    In order to quit the program the user has to enter *quit* instead of a number.

Rollercoaster on the Christmas Market in Tübingen
-------------------------------------------------

.. attention:: Exercise 3.3:

    Ultimate goal of this exercise is that your write a code that calculates how much a group of people pay to
    take a ride on the rollercoaster. To save you from calculating it for every individual and summing that up,
    you should use what you learned about loops and lists and write a code. This exercise should be solved in
    two stages. First write a code that asks the user for age of a person. Using this input your code needs to
    print out how much that person has to pay to ride on the rollercoaster. In the next stage create a list of
    20 randomly chosen ages and change your code so it calculates the sum of all the ticket prices that group
    of 20 people would pay to ride on the rollercoaster.

    .. image:: rollercoaster.png

