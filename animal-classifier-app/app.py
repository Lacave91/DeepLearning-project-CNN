import gradio as gr
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load model
model = tf.keras.models.load_model("vgg16_animal_classifier.keras", safe_mode=False)

# Define class labels (same order as training)
class_labels = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']

# Prediction function
def predict(img):
    img = img.resize((128, 128))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    preds = model.predict(img_array)[0]
    return {class_labels[i]: float(preds[i]) for i in range(10)}

# Gradio interface
interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="🐾 Animal Classifier",
    description="Upload an animal image to classify it using a VGG16-based model.",
    allow_flagging="never"
)

if __name__ == "__main__":
    interface.launch()