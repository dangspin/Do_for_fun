from tensorflow.keras.models import Model as KerasModel
from tensorflow.keras.layers import Input, Dense, Activation, Reshape,Concatenate, Dropout, concatenate
from tensorflow.keras.layers import Embedding
# from keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import plot_model

from keras import backend as K

## Model 1. Multilayer Perceptron
## Parameter: 10 inputs 3 hidden layers, 10, 20, 10 neurons. 1 output with Sigmoid activation

data_input = Input(shape = (10,))
hidden = Dense(10, activation = 'relu')(data_input)
hidden = Dense(20, activation = 'relu', activity_regularizer=regularizers.l1(0.01))(hidden)
hidden = Dense(10, activation = 'relu')(hidden)
output = Dense(1, activation = 'sigmoid')(hidden)
model = KerasModel(inputs = data_input, outputs = output)

## Plot the model out
plot_model(model, show_shapes=True, show_layer_names=True, to_file='multilayer_perceptron_graph.png')
from IPython.display import Image
Image(retina=True, filename='multilayer_perceptron_graph.png')
