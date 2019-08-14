# -*- coding: utf-8 -*-
#%% MNIST MLP 예제 https://3months.tistory.com/54?category=755917 [Deep Play]
# -*- coding: utf-8 -*-
#예제 https://pinkwink.kr/1121

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
import numpy as np
import matplotlib.pyplot as plt 

#%%

#%% KERAS에서 제공하는 MNIST DATA SET 받아오기
img_rows = 784
#img_cols = 28

#데이터 구조 확인 해보기
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()


#%%
input_shape = (img_rows)
x_train = x_train.reshape(x_train.shape[0], img_rows)
x_test = x_test.reshape(x_test.shape[0], img_rows)

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

batch_size = 128
num_classes = 10
epochs = 12

y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

#%%
# multi-layer perceptron

seed = 7
np.random.seed(seed) #난수에 대한 초기값을 고정(프로그함램 실행할 때마다의 결과를 동일하도록 하기 위)

print (type(x_train))
print (type(y_train))

# y_test 의 column을 클래스의 갯수 지정 : 10개
num_classes = y_test.shape[1]
num_pixels = x_train.shape[1]

#%%

# define baseline model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(num_pixels, input_dim=num_pixels, init='normal', activation='relu'))
    model.add(Dense(num_classes, init='normal', activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def good_model():
    # create model
    model = Sequential()
    model.add(Dense(400, input_dim=num_pixels, init='normal', activation='relu'))
    model.add(Dense(100, init='normal', activation='relu'))
    model.add(Dense(num_classes, init='normal', activation='softmax'))
    # Compile model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


#%% Single layer
# build the model
model = baseline_model()
# Fit the model
model.fit(x_train, y_train, validation_data=(x_test, y_test), nb_epoch=epochs, batch_size=batch_size, verbose=2)
# verbose
# Final evaluation of the model
scores = model.evaluate(x_test, y_test, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))

#%%
model.summary()

#%%
n = 15
plt.imshow(x_test[n].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()

test_labels = np.argmax(y_test, axis=1)
predicted_result = model.predict(x_test)
predicted_labels = np.argmax(predicted_result, axis=1)

print('The Answer is ', predicted_labels[n])
tmp = "Label:" + str(test_labels[n]) + ", Prediction:" + str(predicted_labels[n])
plt.title(tmp)


#%% 2 Hidden layer
# build the model
model2 = good_model()
# Fit the model
model2.fit(x_train, y_train, validation_data=(x_test, y_test), nb_epoch=epochs, batch_size=batch_size, verbose=2)
# Final evaluation of the model
scores = model2.evaluate(x_test, y_test, verbose=0)
print("Baseline Error: %.2f%%" % (100-scores[1]*100))

#%%
model2.summary()

#%%
n = 15
plt.imshow(x_test[n].reshape(28, 28), cmap='Greys', interpolation='nearest')
plt.show()

test_labels = np.argmax(y_test, axis=1)
predicted_result = model2.predict(x_test)
predicted_labels = np.argmax(predicted_result, axis=1)

print('The Answer is ', predicted_labels[n])
tmp = "Label:" + str(test_labels[n]) + ", Prediction:" + str(predicted_labels[n])
plt.title(tmp)


#%%
