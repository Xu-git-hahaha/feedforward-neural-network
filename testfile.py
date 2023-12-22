import neural_network2
import neual_net
import os
import pickle

import torch
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
import matplotlib.pyplot
from matplotlib import pyplot

path = "/Users/xuguoxiang/Desktop/feedforword neural network/model.pkl"
input_nodes = 784
hidden_nodes = 200
output_nodes = 10

# learning rate
learning_rate = 0.1

# create instance of neural network
n = neual_net.neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
n = neural_network2.load_param(n,path)

test_data_file = open("/Users/xuguoxiang/Desktop/feedforword neural network/value.txt", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

all_values = test_data_list[0].split(',')
print(all_values)
image_array = numpy.asfarray(all_values[0:]).reshape((28,28))
#print('test nunber is:',all_values[0])
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
pyplot.show()
outputss = n.query((numpy.asfarray(all_values[0:]) / 255.0 * 0.99) + 0.01)
outputlabel = numpy.argmax(outputss)
print('test result is:',outputlabel)
'''if int(outputlabel) == int(all_values[0]):
    print('Test successfully!')
else:
    print('Wrong~')
'''