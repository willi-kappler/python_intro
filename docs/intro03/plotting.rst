How to plot data
================

.. index::
    single: plot
    single: title
    single: xlabel
    single: ylabel
    single: show

When ploting in python we use the ``plot()`` function part of the matplotlib library. In the plot function you give the
X and Y parameter. Remember that X and Y need to have the same length. using ``plt.title``, ``plt.xlabel`` and ``plt.ylabel``
you define a title, x and y labels. In this class as well as outside of this class, for your thesis or reports, a
plot always needs axes labels and ideally a title and a legend. You need the ``plt.show()`` comment at the
end, which tells python to plot the data in the format you specified before:

.. code-block:: python

    # Import both modules:
    import matplotlib.pyplot as plt
    import numpy as np

    # E.g. salinity vs temperature:
    array2D=np.array([[5.2, 3.0, 4.5], [9.1, 0.1, 0.3]])

    # Plotting point data, make sure that both vectors you want to plot have the same length:
    temp=array2D[0, :]
    sal=array2D[1, :]

    plt.plot(temp, sal, "o")
    plt.title("Salinity vs Temp in the Atlantic")
    plt.xlabel("temperature")
    plt.ylabel("salinity")
    plt.grid()

    ax.set(xlabel="Time in years", ylabel="Co2 in ppm", title="Keeling Curve")
    plt.show()



The default of the ``plot()`` function is to draw a line. The style of the line can be changed using:

.. code-block:: python

    plt.plot(x, y, linestyle=":", color="b") # Dotted blue line
    plt.plot(x, y, linestyle="-.", color="y") # Dash-Dot yellow line
    plt.plot(x, y, linestyle="--", color="g") # Dashed green line

You can read more about line styles here: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html

.. index::
    single: savefig
    single: png
    single: pdf

Exporting plots
---------------

In order to save a plot you are creating in python simply use the ``plt.savefig("name.png")`` for a png-file or ``plt.savefig("name.pdf")``
for a pdf file:

.. code-block:: python

    import matplotlib.pyplot as plt

    # Setting the size of the figure -important in case you want this to fit perfectly your page
    fig, ax = plt.subplots(figsize=(10, 6))

    x = [1, 2, 3, 4, 5, 6]
    y = [0, 2, 4, 6, 8, 10]

    # Plotting the data
    ax.plot(x, y)

    ax.set_title("Title", fontsize=20)
    ax.set_xlabel("Time", fontsize=16)
    ax.set_ylabel("Intensity", fontsize=16)
    plt.savefig("my_plot.png")

