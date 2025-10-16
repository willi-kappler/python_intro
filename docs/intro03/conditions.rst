If conditions
=============

.. index::
    single: if
    single: elif
    single: else

Important for the if conditions and for the for loop is to have a colon after the statement and then have eveything in
this block indented. So do no introduce additionsl indentations, this will cause an error.

.. code-block:: python

    # Defining an if condition, this could also be used to compare two variables

    a = 2
    if a > 10 and a <= 50:
        print("a is large")
    elif a > 50:
        print("a is very large")
    else:
        print("a is small")

Here is a table of boolean operation that Python supports:
(All of them support short circuit)

.. index::
    single: and
    single: or
    single: any
    single: all

.. _and_or:

.. csv-table:: And, Or
    :header: "a", "b", "a and b", "a or b"
    :align: center

    "False", "False", "False", "False"
    "False", "True", "False", "True"
    "True", "False", "False", "True"
    "True", "True", "True", "True"

.. _any_all:

.. csv-table:: Any, All
    :header: "l", "any(l)", "all(l)"
    :align: center

    "[]", "False", "False"
    "[False]", "False", "False"
    "[True]", "True", "True"
    "[False, True]", "True", "False"
    "[True, False]", "True", "False"
    "[True, True]", "True", "True"
    "[False, False, True]", "True", "False"
    "[True, True, True]", "True", "True"
    "[..., True, ...]", "True", "False"
    "[..., False, ...]", "True", "False"

For loops and if conditions
---------------------------

Now let's combine a for loop and if condition to solve the following exercise.

.. _exercise_3_1:

.. attention:: Exercise 3.1:

    * Create a vector including numbers from 1 to 9.
    * Using a for loop iterate over each of these numbers.
    * If the number is odd (which you can check using the ``%`` (modulus) operator) then add a 1 to the number and print the number.
    * If the number is even then simply print this number.

