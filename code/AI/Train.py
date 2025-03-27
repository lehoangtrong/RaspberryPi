import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras import layers, models

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

train_size = int(0.5 * X_train.shape[0])  
test_size = int(0.5 * X_test.shape[0])    

X_train = X_train[:train_size]
y_train = y_train[:train_size]
X_test = X_test[:test_size]
y_test = y_test[:test_size]

X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

print(f"S? lu?ng m?u hu?n luy?n: {X_train.shape[0]}")
print(f"S? lu?ng m?u ki?m tra: {X_test.shape[0]}")

model = models.Sequential([
    layers.Conv2D(16, (3,3), padding='same', activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D(),
    layers.Conv2D(32, (3,3), padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(10)  # 10 classes
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

epochs = 3  
model.fit(X_train, y_train, epochs=epochs, validation_data=(X_test, y_test))


model.save("/home/admin/Ten/cifar10_model.keras")
print("H")
