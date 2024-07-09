import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

train_data = ImageDataGenerator(rescale = 1./255, validation_split = 0.2)

train_generator = train_data.flow_from_directory(
    "images\_train_data",
    target_size = (150, 150),
    batch_size = 32,
    class_mode = 'categorical',
    subset = 'training') 

validation_generator = train_data.flow_from_directory(
    'images\_rps-cv-images',
    target_size = (150, 150),
    batch_size = 32,
    class_mode = 'categorical',
    subset = 'validation'
)
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation = 'relu', input_shape = (150, 150, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation = 'relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64, (3, 3), activation = 'relu'),
    layers.Flatten(),
    layers.Dense(64, activation = 'relu'),
    layers.Dense(3, activation = 'softmax')

])

model.compile(optimizer = 'adam', 
              loss ='categorical_crossentropy',
              metrics = ['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch = train_generator.samples // 32,
    epochs = 15,
    validation_data = validation_generator,
    validation_steps = validation_generator.samples // 32
)

model.save('rps_model.h5')
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.savefig('training_results.png')