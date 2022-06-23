from keras.models import Sequential
from keras.layers import Flatten, Dense, Conv2D, MaxPooling2D
import os

num_classes = 10
img_width, img_height = 64, 64


def create_model():
    result = Sequential()

    result.add(Conv2D(16, kernel_size=[4, 4], activation='relu', input_shape=(img_width, img_height, 1)))
    result.add(MaxPooling2D(pool_size=[2, 2]))
    result.add(Conv2D(32, kernel_size=[4, 4], activation='relu'))
    result.add(MaxPooling2D(pool_size=[2, 2]))
    result.add(Conv2D(64, kernel_size=[4, 4], activation='relu'))
    result.add(MaxPooling2D(pool_size=[2, 2]))
    result.add(Conv2D(128, kernel_size=[4, 4], activation='relu'))
    result.add(MaxPooling2D(pool_size=[2, 2]))

    result.add(Flatten())
    result.add(Dense(32, activation='relu'))
    result.add(Dense(num_classes, activation='softmax'))

    result.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return result


model = create_model()
model.load_weights(os.path.join(os.getcwd(), "model.h5"))
