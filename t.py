from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.preprocessing.image import ImageDataGenerator

# Define the model architecture
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Define the data generator
train_datagen = ImageDataGenerator(rescale=1./255)

# Load the images from the folder
train_generator = train_datagen.flow_from_directory(
        'path/to/folder',
        target_size=(28, 28),
        batch_size=32,
        color_mode='grayscale',
        class_mode='categorical')

# Train the model
model.fit_generator(
        train_generator,
        steps_per_epoch=2000,
        epochs=10)