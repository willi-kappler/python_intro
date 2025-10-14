Derivatives
===========

Calculating the time (or spatial) derivative of a 1D dataset is something that may occur quite frequently.
Occuring tasks are best written in functions for many reasons (name at least two). Write a function called
``ForwardDifferencingXY`` that takes a **2 x n array** as input where the independent variable (e.g., time) is
stored in the first column, and the dependent variable (e.g., :math:`CO_2` ) in the second column. The output
should also be a **2 x n array** with the independent variable in the first column and the derivative of the
dependent variable in the second colum.
Here you should do this for the Keeling curve and for the Gausspeak.

.. attention:: Exercise 4.9:

    * Use your function ``ForwardDifferencingXY`` to calculate rates of change for the Keeling curve, the
      sinoid and the 1D Gauss Peak.
    * Make your function more robust so that it catches wrong use interactions (e.g., passing
      on a **n x 2 array** instead of **2 x n array**).
    * Make your user function more user friendly by providing an optional figure with sub-panels showing
      the original data on top, and the time derivative at the bottom.
    * Add noise to your input data using numpys ``randn`` function, what does that do to your
      derivatives. Why?
