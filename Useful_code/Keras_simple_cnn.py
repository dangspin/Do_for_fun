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

## Parameter: 64*64, 3 color channel inputs
##           Convolution layer, 32 filters, 4*4
##           MaxPooling layer, 2*2
##           Convolution layer, 16 filters, 4*4
##           MaxPooling layer, 2*2
##           Flatten Lyaer
##           Dense layer, 10 neuron
##           Dense layer, 1 neuron


cnn_input = Input(shape = (64, 64, 1))
cnn_layer = Conv2D(filters = 32, kernel_size = 4)(cnn_input)
cnn_layer = Activation("relu")(cnn_layer)
cnn_layer = MaxPooling2D(pool_size = (2,2))(cnn_layer)
cnn_layer = Conv2D(filters = 16, kernel_size = 4, activation = 'relu')(cnn_layer)
cnn_layer = MaxPooling2D(pool_size = (2,2))(cnn_layer)
flat = Flatten()(cnn_layer)
dense = Dense(10, activation = 'relu')(flat)
output = Dense(1, activation = 'sigmoid')(dense)

model = KerasModel(inputs = cnn_input, outputs = output)

## print model summary
print(model.summary())


## Plot the model
plot_model(model, show_shapes=True, show_layer_names=True, to_file='simple_cnn.png')
from IPython.display import Image
Image(retina=True, filename='simple_cnn.png')
