from matplotlib import pyplot as plt
import numpy as np
#import pandas.rpy.common as rcom
import pandas as pd
#We load the data with load_iris from sklearn
from sklearn.datasets import load_iris
data = load_iris()
x=data.data[:,:2]  # we only take the first two features
print (x[:,0])

plt.scatter(x[:,0], x[:,1], s=10,color='red')
plt.title("graph1")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()
# load_iris returns an object with several fields
features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names
for t in range(3):
    if t == 0:
        c = 'r'
        marker = '>'
    elif t == 1:
        c = 'g'
        marker = 'o'
    elif t == 2:
        c = 'b'
        marker = 'x'
    plt.scatter(features[target == t,0],
        features[target == t,1],
        marker=marker,
        c=c)
 # We use NumPy fancy indexing to get an array of strings:
labels = target_names[target]
# The petal length is the feature at position 2
plength = features[:, 2]
# Build an array of booleans:
is_setosa = (labels == 'setosa')
# This is the important step:
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()
print('Maximum of setosa: {0}.'.format(max_setosa))
print('Minimum of others: {0}.'.format(min_non_setosa))