from tensorflow.keras.models import Model as KerasModel
from tensorflow.keras.layers import Input, Dense, Activation, Reshape,Concatenate, Dropout, concatenate
from tensorflow.keras.layers import Conv2D, Flatten
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Embedding
# from keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model

from tensorflow.keras import backend as K
from tensorflow.keras import regularizers as regularizers


## Model 2. Very simple CNN

## Parameter: Model inputs:
##           64*64, 3 color channel inputs
##
##           Convolution layer, 32 filters, 4*4
##           MaxPooling layer, 2*2
##           Flatten layer1
##           
##           Convolution layer, 16 filters, 8*8
##           MaxPooling layer, 2*2
##           Flatten Layer2
##           
##           Concatenate
##           
##           Dense layer, 10 neuron
##           Dense layer, 1 neuron


cnn_input = Input(shape = (64, 64, 1))

cnn1 = Conv2D(32, kernel_size=4, activation = 'relu')(cnn_input)
cnn1 = MaxPooling2D(pool_size = (2,2))(cnn1)
cnn1 = Flatten()(cnn1)

cnn2 = Conv2D(16, kernel_size = 8, activation = 'relu')(cnn_input)
cnn2 = MaxPooling2D(pool_size = (2,2))(cnn2)
cnn2 = Flatten()(cnn2)

concats = Concatenate()([cnn1, cnn2])
out_put = Dense(10, activation = 'relu')(concats)
out_put = Dense(1, activation = 'sigmoid')(out_put)

model = KerasModel(inputs = cnn_input, outputs = out_put)

## print model summary
print(model.summary())


## Plot the model
plot_model(model, show_shapes=True, show_layer_names=True, to_file='simple_cnn.png')
from IPython.display import Image
Image(retina=True, filename='simple_cnn.png')
