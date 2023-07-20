
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import tensorflow as tf
import numpy as np

def getPrediction(trained_model_path, img_path):
    print(img_path)
    img = tf.keras.utils.load_img(img_path)

    img = tf.keras.preprocessing.image.smart_resize(img, (224, 224), interpolation='bilinear')

    img_array = tf.keras.preprocessing.image.img_to_array(img)

    img_array = tf.expand_dims(img_array, 0)
    model = load_model(trained_model_path)
    class_names = ['Apple Scab', 'Apple Black rot', 'Apple Cedar Apple Rust', 'Apple healthy', 'Background Without Leaves', 'Blueberry Healthy', 'Cherry Powdery Mildew', 'Cherry Healthy', 'Corn Cercospora Leaf Spot Gray Leaf Spot', 'Corn Common Rust', 'Corn Northern Leaf Blight', 'Corn Healthy', 'Grape Black Rot', 'Grape Esca (Black Measles)', 'Grape Leaf Blight (Isariopsis Leaf Spot)', 'Grape Healthy', 'Orange Haunglongbing (Citrus Greening)', 'Peach Bacterial spot', 'Peach Healthy', 'Bell Pepper Bacterial Spot', 'Bell Pepper Healthy', 'Potato Early Blight', 'Potato Late Blight', 'Potato Healthy', 'Raspberry Healthy', 'Soybean Healthy', 'Squash Powdery Mildew', 'Strawberry Leaf Scorch', 'Strawberry Healthy', 'Tomato Bacterial Spot', 'Tomato Early Blight', 'Tomato Late Blight', 'Tomato Leaf Mold', 'Tomato Septoria Leaf Spot', 'Tomato Spider Mites Two Spotted Spider Mite', 'Tomato Target Spot', ' Tomato Yellow Leaf Curl Virus', 'Tomato Mosaic Virus', 'Tomato Healthy']
    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]

    confidence = round(100 * (np.max(predictions[0])), 2)

    return predicted_class