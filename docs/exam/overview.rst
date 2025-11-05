Oral exam exercises
===================

Prepare this small project as a conversation starter for the oral exam of your group.
Note, this will only be a conversation starter and does not exhaustively cover all possible questions during the exam.
Your code must include comments: a header with your names, and some short descriptions.
Do the extra work only if you want to have a grade better than 1.7! For all the extra work all the user input must be checked for errors
and a proper error message must be given. Each group has to hand in their code via email to
amirhossein.ershadi@uni-tuebingen.de.
You can find the groups, data files, exam dates and the dead lines on Ilias.



Exam 01
-------

Nahuelbuta weather station

The data file contains data from a weather station in Nahuelbuta.

* Read in the CSV file ``data1.csv``. (use ``np.loadtxt()`` and ``delimiter=","``)
* Write a function that filters out the invalid values (``-9999.0``) from the data.
* Plot the first (air temperature in :math:`^{\circ} C`) and second column (solar radiation :math:`\frac{W}{m^2}`) in two separate plots.
* The time information is missing, try to figure out from what time period the data is.

Extra work:
Do a polynomial fitting (order two) for two different days. Plot the polynomials and the difference. Add
some interactions to the plots: let the user specify the time range via a slider.

Exam 02
-------

A GPS Station in Antarctica

Load data ``data2.txt``. This datafile was recoreded by a GPS station on an Antarctica Ice
shelf. The data structure is as follows:

* col1: coordinate polar stereographic East (m)
* col2: coordinate polar stereographic South (m)
* col3: coordinate longitude (decimal degrees)
* col4: coordinate latitude (decimal degrees)
* col5: elevation (m, relative to WGS84)
* col6: days (relative to an arbitrary date in the past)

Visual the vertical coordinate as a function of time. Visualize the horizontal trajectory of the station.
Fit a linear regression line to the horizontal trajectory. What is the approximate speed in meters per year?

Extra work:
Plot the elevation as a function of distance. Make the plot interactive: let the user change the distance
range via a slider.

Exam 03
-------

Min, Max, Mean

* Read in data from the user as input from the command line. If the user types ``x`` stop reading.
* Write a function that calculates the min, max and mean values from that input. The function should return a tuple (a, b, c) containing the three values
* Print the values at the end

Extra work:
Add another input for the column number. Then read multiple files and concatenate all the data of the
specified column together. Use your function to determine the min, max and mean values of that data.

Exam 04
-------

Daily average

The data given is from one year (2017) of the weather station in Santa Gracia. There are 24 values per
day (1 hour average).

* Read in the CSV file ``data4.csv``. (use ``np.loadtxt()``, ``delimiter=","`` and ``usecols=(1,2)``)
* Write a function that filters out the invalid values (-9999.0) from the data.
* Write a function that calculates the average for each day (average over 24 values).
* Plot the data: first column contains air temperature, second column contains air relative humidity.

Extra work:
Calculate the correlation of both data sets. Make the plot interactive: let the user change the time range
via a slider.

Exam 05
-------

Derivative

The data given is from one year (2018) of the weather station in Santa Gracia. There are 24 values per
day (1 hour average).

* Read in the CSV file ``data5.csv``. (use ``np.loadtxt()``, ``delimiter=","`` and ``usecols=(1,2)``)
* Write a function that filters out the invalid values (-9999.0) from the data.
* Write a function that calculates the first and second derivative.
* Plot the data: first column contains the average wind speed, second column contains the maximum wind speed.

Extra work:
Calculate the correlation of both data sets. Make the plot interactive: let the user change the time range
via a slider.

Exam 06
-------

Smoothing Data

Load data ``data6.txt``. This datafile was recoreded by a GPS station on an Antarctica Ice
shelf. The data structure is as follows:

* col1: coordinate polar stereographic East (m)
* col2: coordinate polar stereographic South (m)
* col3: coordinate longitude (decimal degrees)
* col4: coordinate latitude (decimal degrees)
* col5: elevation (m, relative to WGS84)
* col6: days (relative to an arbitrary date in the past)

Visualize the vertical displacement as a function of time. The data are a bit noisy for your liking. Smooth
the data with a running mean. This means, write a for loop that goes through the data and for each point
in time you average values in its surrounding. This is called a running mean. It is not the best way to
smooth data, but a good exercises. Write your own loop, don’t use external functions.

Extra work:
Find a better way to do the smoothing (search online). Make the plot interactive: let the user change the
time range via a slider.

Exam 07
-------

A bit of geophysics, but not too much.

The data file (``data7.txt``) is a derived product from a radar survey in Antarctica. The radar was towed behind a skidoo
with lots of driving around. The data format is as follows:

* col1: coordinate polar-stereographic East (m)
* col2: coordinate polar-stereographic South (m)
* col3: two-way traveltime to a sub-surface reflector (seconds)

Filter out all the NaN values. Visualize the skidoo-tracks in an x-y plot. Write a function that converts
the two-way traveltime of the sub-surface reflector to a depth below the surface. Assume a radio-wave
velocity of :math:`1.72 · 10^8 \frac{m}{s}`. What is the average depth of the sub-surface reflector in meters? Can you
visualize this using the scatter function in matplotlib?

Extra work:
Calculate the distance along the radar track and plot the ice thickness over distance. Import a satellite
image and plot the x and y coordinate onto this.

Exam 08
-------

Polynomial

The data (``data8.csv``) given is from one month (2022.04) of the weather station in Nahuelbuta. There are 24 values
per day (1 hour average).

* Read in the CSV file "data5.csv". (use np.loadtxt(), delimiter="," and usecols=(1,2))
* Write a function that filters out the invalid values (-9999.0) from the data.
* Take one of the precipitation peaks (for example on 2022-04-24) and try to fit a second order polynomial using the function polyfit.
* Plot the data: first column contains the solar radiation, second column contains the precipitation.

Extra work:
Write a function that takes the data and calculates (and returns) the min, max and mean values. Make
the plot interactive: let the user change the time range via a slider.

Exam 09
-------

A bit of geophysics, but not too much.

The data file (``data9.txt``) is a derived product from a radar survey in Antarctica. The radar was towed behind a skidoo
with lots of driving around. The data format is as follows:

* col1: coordinate polar-stereographic East (m)
* col2: coordinate polar-stereographic South (m)
* col3: two-way traveltime to a sub-surface reflector (seconds)

Filter out all the NaN values. Visualize the skidoo-tracks in an x-y plot. Write a function (containing a for
loop) that calculates the total distance travelled. The function should stop the calculation if the distance
between two datapoints is larger than 500 m.

Extra work:
Import a satellite image and plot the x and y coordinate onto this. Make this plot interactive so that the
user can change the stop value for the distance (500 m).
