from tensorflow.keras.models import Model as KerasModel
from tensorflow.keras.layers import Input, Dense, Activation, Reshape,Concatenate, Dropout, concatenate
from tensorflow.keras.layers import Conv2D, Flatten
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Embedding
# from keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model

from tensorflow.keras import backend as K
from tensorflow.keras import regularizers as regularizers


## Model 2. Very simple LSTM

## Parameter: 100 time steps (recursive 100 time points), 1 input feature
##            LSTM layer, hidden units = 10, output units = 10, Ct-1 units = 10
##            Dense layer, 10 neuron
##            Dense layer, 1 neuron


lstm_input = Input(shape = (100, 1))
lstm_layer = LSTM(unit = 10)(lstm_input)  ## No need to use the key word input_shape, since lstm is not the first layer in this example
dense = Dense(10, activation = 'relu')(lstm_layer)
output = Dense(1, activation = 'sigmoid')(dense)

model = KerasModel(inputs = lstm_input, outputs = output)

## print model summary
print(model.summary())


## Plot the model
plot_model(model, show_shapes=True, show_layer_names=True, to_file='simple_lstm.png')
from IPython.display import Image
Image(retina=True, filename='simple_lstm.png')
