## This script is used to illustrate the fancy indexing of numpy

import numpy as np

a = np.array([[1,2,3,4,5],[6,7,8,9,10],
             [11,12,13,14,15],[16,17,18,19,20],
             [21,22,23,24,25]])
             
b = a[[1,2,3],[2,4, 4]]

## array([ 8, 15, 20])

a[[0,1,2,3,4],[2,2,2,2,2]] = 1
print(a)

## array([[ 1,  2,  1,  4,  5],
##       [ 6,  7,  1,  9, 10],
##       [11, 12,  1, 14, 15],
##       [16, 17,  1, 19, 20],
##       [21, 22,  1, 24, 25]])


## Example 1: Binning Data

x = np.random.randn(100)

# compute a histogram by hand
bins = np.linspace(-5, 5, 20)
print(bins)
## array([-5.        , -4.47368421, -3.94736842, -3.42105263, -2.89473684,
##        -2.36842105, -1.84210526, -1.31578947, -0.78947368, -0.26315789,
##         0.26315789,  0.78947368,  1.31578947,  1.84210526,  2.36842105,
##         2.89473684,  3.42105263,  3.94736842,  4.47368421,  5.        ])

counts = np.zeros_like(bins)

# find the appropriate bin for each x
i = np.searchsorted(bins, x)
print(i)

## array([ 7,  9,  9,  8, 10, 11, 14, 10, 10, 10,  6, 10, 10, 15, 10, 11, 10,
##         8, 12, 11, 12,  8, 13,  7, 11, 14,  8,  9, 10,  9,  7, 10,  8, 11,
##         8, 13,  9,  9, 12,  8, 10, 12,  7, 10, 10, 11,  8,  7, 11, 11, 10,
##        11,  9, 10, 11,  9, 14, 11,  8, 11,  8, 11, 12,  8, 12, 11, 12, 14,
##        10,  9,  8,  8, 10, 11, 11, 12, 10, 13,  9, 15, 11,  8,  8, 11, 10,
##        11, 11, 10,  8,  7,  9, 12, 10,  8, 10, 11,  8, 10, 10,  8])

# add 1 to each of these bins
np.add.at(counts, i, 1)


## Example 2: to categorical one-hot encoding
def to_categorical(y, dtype = 'float32'):
    
    y = np.array(y, dtype = int)
    
    input_shape = y.shape
    
    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])   ## get the real dimension of input since a dim = 1 is useless
        
    y = y.ravel()
    
    num_classes = np.max(y) + 1
    n = input_shape[0]
    
    categorical = np.zeros((n, num_classes), dtype = dtype)
    categorical[np.arange(n), y] = 1
    
    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)
    return categorical
