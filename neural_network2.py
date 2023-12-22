import os
import dill as pickle

import torch
import numpy
# scipy.special for the sigmoid function expit()
import scipy.special
import matplotlib.pyplot
from matplotlib import pyplot

import neual_net

from torch import nn,optim
import torch.nn.functional as F
#from torch.autograd import Variable
#from torchvision import datasets, transforms

# neural network class definition

def load_param(model,path):
    if os.path.exists(path):
        try:
            file = open(path, 'rb')
            model = pickle.load(file)
        except EOFError:
            return 'empty'
    return model
def save_param(model,path):
    file = open(path,'wb')
    pickle.dump(model,file)
    file.close()

# number of input, hidden and output nodes
if __name__ == '__main__':
    input_nodes = 784
    hidden_nodes = 200
    output_nodes = 10

    # learning rate
    learning_rate = 0.1

# create instance of neural network
    n = neual_net.neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# load the mnist training data CSV file into a list
    training_data_file = open("mnist_dataset/mnist_train.csv", 'r')
    training_data_list = training_data_file.readlines()
    training_data_file.close()
# train the neural network

# epochs is the number of times the training data set is used for training
    epochs = 8

    for e in range(epochs):
    # go through all records in the training data set
        for record in training_data_list:
        # split the record by the ',' commas
            all_values = record.split(',')
        # scale and shift the inputs
            inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        # create the target output values (all 0.01, except the desired label which is 0.99)
            targets = numpy.zeros(output_nodes) + 0.01
        # all_values[0] is the target label for this record
            targets[int(all_values[0])] = 0.99
            n.train(inputs, targets)
            pass
        print('training~~~')
        pass

    save_param(n,"/Users/xuguoxiang/Desktop/feedforword neural network/model.pkl")

#load_param(n,"/Users/xuguoxiang/Desktop/feedforword neural network/model.pkl")
# load the mnist test data CSV file into a list
    test_data_file = open("/Users/xuguoxiang/Desktop/feedforword neural network/testvalue.txt", 'r')
    test_data_list = test_data_file.readlines()
    test_data_file.close()
# test the neural network


'''
# scorecard for how well the network performs, initially empty
scorecard = []

# go through all the records in the test data set
for record in test_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # correct answer is first value
    correct_label = int(all_values[0])
    # scale and shift the inputs
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = n.query(inputs)
    # the index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
    # append correct or incorrect to list
    if (label == correct_label):
        # network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        # network's answer doesn't match correct answer, add 0 to scorecard
        scorecard.append(0)
        pass

    pass
# calculate the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
print("performance = ", scorecard_array.sum() / scorecard_array.size)

'''



'''
all_values = test_data_list[0].split(',')
print(all_values)
image_array = numpy.asfarray(all_values[1:]).reshape((28,28))
print('test nunber is:',all_values[0])
matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
pyplot.show()
outputss = n.query((numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01)
outputlabel = numpy.argmax(outputss)
print('test result is:',outputlabel)
if int(outputlabel) == int(all_values[0]):
    print('Test successfully!')
else:
    print('Wrong~')
'''