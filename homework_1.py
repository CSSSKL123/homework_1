import numpy as np
import matplotlib.pyplot as plt


"""
Verifying whether character is float or not through
a try except, and adding each float to the current
float multiplied by 10 each time to receive the
date as a float point value

Args:
    string_date: a date in the form of year, month
    and date in a string

Returns:
    a floating point value representative of the
    string value argument except without the dashes.
"""
def convert_date_to_float(string_date):
    float_date = 0.0
    for i in string_date :
        try:
            float(i)
            float_date = (float_date * 10) + int(i)
        except ValueError:
            continue

    return float_date


with open('data_file.csv', 'r') as file:
    lines = file.readlines()[1:]

data2 = []

"""
In each line of the data, an array of strings is
created and the first element - the date - is converted
to a floating point element, then the rest of the
elements are changed into floats as well. The elements
of that line are all added to the array in the end.
"""
for line in lines:
    elems = line.strip().split(',')
    elems[0] = convert_date_to_float(elems[0])
    elems = [float(elem) for elem in elems]
    data2.append(elems)
data2 = np.array(data2)

"""
This simple method extracts the data from the csv file
and automatically imports it to the data3 array with the
genfromtxt() method in one line
"""
data3 = np.genfromtxt('data_file.csv', delimiter=',', dtype=float)[1:]


"""
Checking if the two arrays are equal with the allclose method and
starting each row at the second column by slicing it
"""
print(np.allclose(data2[:,1:], data3[:,1:]))


"""
The trading day and adjusted close arrays are the first and last columns
of the array and CSV file, so the data was sliced to retrieve just those
two subarrays. The days since 1950 array is created using the arange function
and inputting the trading_day array length as the length of this array too
"""
trading_day = data2[:, 0]
adjusted_close = data2[:, -1]
days_since_1950 = np.arange(len(trading_day))
plt.plot(days_since_1950, adjusted_close)
plt.xlabel('Trading Days Since Jan 3, 1950')
plt.ylabel('Adjusted Close[USD]')
plt.title('S&P 500 Index Daily Close')
plt.show()


"""
Same computation as the first graph, except the adjusted close array is
replaced with a difference between the high column and low column in the
data file. The remaining values stayed the same for both graphs.
"""
trading_day = data2[:, 0]
difference = data2[:, 2] - data2[:, 3]

days_since_1950 = np.arange(len(trading_day))
plt.plot(days_since_1950, difference)
plt.xlabel('Trading Days Since Jan 3, 1950')
plt.ylabel('Daily High-Low [USD]')
plt.title('S&P 500 Index Daily High Minus Low')
plt.show()

