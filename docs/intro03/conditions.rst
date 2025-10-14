If Conditions
=============

Important for the if condition as for the for loop is to have a colon after the if condition and then have eveything in
this condition indented. So do no introduce additionsl indentations, this will cause an error.

.. code-block:: python

    # Defining an if condition, this cousd also be used to compare two variables

    a = 2
    if a > 10 and a <= 50:
        print("a is large")
    elif a > 50:
        print("a is very large")
    else:
        print("a is small")

For loops and if conditions
===========================

Now let's combine a for loop and if condition to solve the following exercise.

.. attention:: Exercise 3.1:

    * Create a vector including numbers from 1 to 9.
    * Using a for loop iterate over each of these numbers.
    * If the number is odd (which you can check using the ``%`` (modulus) operator) then add a 1 to the number and print the number.
    * If the number is even then simply print this number.

