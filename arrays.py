import matplotlib.pyplot
import numpy
from matplotlib import pyplot

a = numpy.zeros( [3,2] )
print(a)
a[0,0] = 3
a[1,1] = 2
a[1,0] = 1
a[2,0] = 5
a[0,1] = 8
a[2,1] = 15
matplotlib.pyplot.imshow(a, interpolation="nearest")
pyplot.show()