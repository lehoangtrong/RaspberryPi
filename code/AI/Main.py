import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

model = tf.keras.models.load_model("/home/admin/Ten/cifar10_model.keras")
model.summary()

class_names = ["May bay", "Xe hoi", "Chim", "Meo", "Huou", "Cho", "Ech", "Ngua", "Tau", "Xe tai"]

def detect_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    img = cv2.resize(img, (32, 32))  
    img = img.astype("float32") / 255.0  

    img_array = np.expand_dims(img, axis=0)

    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)

    plt.imshow(img)
    plt.title(f"Du doan: {class_names[predicted_class]}")
    plt.axis("off")
    plt.show()

    return class_names[predicted_class]

image_path = "/home/admin/Ten/con-meo-235298441.jpg"  
result = detect_image(image_path)
print(f"Ket Qua: {result}")
