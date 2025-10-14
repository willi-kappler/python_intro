Math functions
==============

Visualization of mathematical functions
---------------------------------------

Make use of some numpy functions (``numpy.arange``) and get a feel for some vector manipulation.

.. attention:: Exercise 4.6:

    * Visualize :math:`f(t)=\sin(\omega t + \phi_0)` for a given frequency :math:`\omega = 1.2Hz` and phase shift :math:`\phi_0` over the time
      interval :math:`t = 0...10` at discrete time intervals :math:`dt = 0.001` s.
    * Visualize :math:`f^2(t)`. What happens if you reduced dt to 1 s ?
    * Visualize a Gaussian peak:

      .. math::
        f(x) = Ae^{-\frac{(x-x_0)^2}{\sigma_x}}

      where x is the independent variable and the factors :math:`x_0` , :math:`A`, and :math:`\sigma_x` determine the shape of the function.
      Make sure that you understand what each parameter pertains to.

More Loops
----------

.. attention:: Exercise 4.7:

    Visualize a 2D Gaussian peak:

    .. math::
        f(x,y) = Ae^{-\frac{(x-x_0)^2}{\sigma_x}-\frac{(y-y_0)^2}{\sigma_y}}

    using a nested for loop. This is harder. In essence you will need to fill a 2D array and visualize it with colors
    using ``plt.pcolormesh()``. Then do the same but replace the nested for loops using numpys ``"meshgrid"``.
    What is easier?

Recursion
---------

There is a third way to do loops in Python (and other programming languages as well): If you define a
function you can call that function recursively:

.. code-block:: python

    def Fibonacci(n):
        if n < 0:
            raise ValueError(f"Negative numbers are not allowed: {n}")
        elif n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Fibonacci(n - 1) + Fibonacci(n - 2)

    print(f"F0: {Fibonacci(0)}")
    print(f"F1: {Fibonacci(1)}")
    print(f"F2: {Fibonacci(2)}")
    print(f"F3: {Fibonacci(3)}")
    print(f"F9: {Fibonacci(9)}")

Mathematically the Fibonacci numbers are defined as:

.. math::
    F_{n} = \left\{
        \begin{array}{ll}
            0, & n = 0 \\
            1, & n = 1 \\
            F_{n-1} + F_{n-2}, & n > 1
        \end{array}
    \right.

.. attention:: Exercise 4.8:

    Now write the Fibonacci function in a non-recursive way using a *for loop* or a *while loop*.

Regressions
-----------

Regression analysis is a way to determine a realtion between different parameters or variables. Such a relation might
be linear (first order) or polynominal (higher order). To determine how good the fit of the regression is to the actual
data, we can calcualte the R2 value. The higher the R2 value, the better the fit to the data. Let's look at Figure below.
Here the green dots are our exemplary datapoint. Panel 1 shows a linear fit, Panel 2 a second order, Panel 3 a third
oder and Panel 4 a forth order fit. We see the R2 value increasing with every panel. In this example the exemplary
data is created using a forth order polinominal function.

Using the polyfit function you can fit a n-th order function to your data. The output of this function then is a vector
of coefficients p that minimise the squared error of the fit to the data. For instance for a linear fit the fit looks like:

TODO ...

