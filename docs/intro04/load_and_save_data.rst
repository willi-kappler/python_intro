Loading and saving data
=======================

.. index::
    single: loadtext
    single: keeling
    single: load
    single: read

Loading and visualization of ASCII-txt input data
-------------------------------------------------

Load the file ``monthly_in_situ_co2_mlo_ready4loading.txt`` which is the Keeling curve. If you don't
know what this is please inform yourself. The data are decimal years in the first column and :math:`CO_2` in ppm
in the second column. A lack of data is marked with negative numbers.

.. _exercise_4_1:

.. attention:: Exercise 4.1:

    * Load the data (e.g., using ``numpy.loadtxt()``).
    * How many datapoints are in the time series? What are the dimensions of the data array?
    * Visualise the data (e.g., using `matplotlib``) with meaningful x- and y-limits and axis labels. Decide
      if the data are better visualised as points, curves or both. Change the color and symbols of the
      points.
    * Using Python functions calculate basic quantities such as the mean, minimum and maximum of your
      time series. Are those values meaningful?
    * Visualize only the first ten elements, the last ten elements, and elements from 20 to 30.

.. index::
    single: filter

Basic filtering and data manipulation
-------------------------------------

Load the Keeling curve again. We have understood that no data values are marked with negative
numbers. Let's remove those with a for loop (there are better ways to do this...).

.. _exercise_4_2:

.. attention:: Exercise 4.2:

    * Print all CO2 values on the screen using a for loop.
    * Print only the time intervals where no data are available
    * Create a new vector where the no-data values are removed.
    * Visualize the new vector. Anything different compared to the previous exercise?
      Start a new for loop block and calculate the time derivative of the time series. Visualize it.

.. index::
    single: read_csv
    single: concat
    single: multiple files

Reading data from multiple files
--------------------------------

At some time you have to read in multiple files one after each other and combine all the data. One way
of doing this is to specify the files in a list:

.. code-block:: python

    import pandas

    files = ["file1.csv", "file2.csv", "more_data.csv", "old_data.csv", "unknown.csv"]

    result = pandas.DataFrame()

    for file in files:
        data = pandas.read_csv(file)
        result = pandas.concat([result, data])

    print(result)

.. index::
    single: glob
    single: pattern

Another way is to specify a file pattern and to load all the files that have that pattern in their name:

.. code-block:: python

    import pandas
    import glob

    files = glob.glob("*.csv")

    result = pandas.DataFrame()

    for file in files:
        data = pandas.read_csv(file)
        result = pandas.concat([result, data])

    print(result)

So now try to do it by yourself: Load in some data files, merge the data and make a nice plot.

.. index::
    single: to_csv
    single: export
    single: write
    single: save

Exporting data from Python
--------------------------

At some point you have to export the results of your calculation into files, which you can then store some-
where. To export data into a csv file you can use the ``.to_csv("filename.csv")`` function. Whenever
you export data, make sure you assign a header to each column. Headers and a appropriate file name
allow you (and others) to be able to understand exported datasets at a later time. Within the ``.to_csv()``
function you can specify a filename, the headers to the columns, the separator etc.

.. code-block:: python

    import math
    import pandas as pd

    def gen_data(filename, start, end, factor):
        data = []
        for x in range(start, end):
            y = math.sin(x * factor)
            data.append((x, y))

        df = pd.DataFrame(data)
        df.to_csv(filename, header=["x", "y"], index=False)

    gen_data("data1.csv", 0, 100, 0.01)
    gen_data("data2.csv", 50, 100, 0.001)
    gen_data("data3.csv", 10, 20, 0.001)
    gen_data("data4.csv", 5, 10, 0.1)

.. _exercise_4_3:

.. attention:: Exercise 4.3:

    To get used to the export and import function go back to the Keeling curve data. Modify the txt file to
    a csv file (e.g. manually in the explorer). Import that csv file using the import csv function. As a next
    step, delete all the negative values and then export the dataset using the export function. Give the data
    a header and give it a sensible name, to make it clear, that the negative values have been deleted from
    this file.

More data manipulation
----------------------

.. _exercise_4_4:

.. attention:: Exercise 4.4:

    Load the file called "temperature_amplitude.txt". This contains two columns, the first has temperature
    in :math:`^{\circ} C`, the second the radar amplitudes of a reflection. The system used for the data acquisition is time
    sensitive. This means whenever the temperature of the surrounding falls below :math:`0^{\circ} C` the amplitude of the
    signal has to be scales up by a factor of 10. Write a code that reads in the data, corrects the data for
    the temperature dependence and then exports the data again in a file that contains headers. To make the
    difference between a while and a for loop more clear, write a code containing a while loop and then one
    that contains a for loop and compare the results.
