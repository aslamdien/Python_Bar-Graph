# Calculate the Mean (average)
import numpy # This make calculating the Mean Easier

marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

my_mean = numpy.mean(marks_of_students)

print("My Mean is: ", my_mean)

# Calculate the Median
marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

my_median = numpy.median(marks_of_students)

print("My Median is: ", my_median)

# Calculate the Mode
from scipy import stats

marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

my_mode = stats.mode(marks_of_students)

print("My Mode is: ", my_mode)

# Calculate the Range
marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

my_range = numpy.ptp(marks_of_students)

print("My Range of the marks is: ", my_range)

# Calculate Inter-quartile Range
marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

my_quartile_range = numpy.percentile(marks_of_students, 25)

print("My Inter-quartile of the marks is: ", my_quartile_range)

# Calculate the Variance
marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

my_variance = numpy.var(marks_of_students)

print("My Variance of the marks is: ", my_variance)

# Calculate the Standard Deviation
marks_of_students = [90, 72, 82, 90, 69, 19, 23, 30, 45, 5]

my_std = numpy.std(marks_of_students)

print("My Standard Deviation is: ", my_std)
