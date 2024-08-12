import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# Loading the model
model = tf.keras.models.load_model('digit-recognizer-model.h5')

def preprocess_image(image):
    # Invert image if needed
    if np.mean(image) > 0.5:  # Simple heuristic: if average pixel value is high, it's likely a white background
        image = 1.0 - image  # Invert the image
    return image

def predict_digit(image):
    # Convert image to grayscale and handle transparency
    if isinstance(image, np.ndarray):
        image = Image.fromarray(image).convert('L')
    else:
        image = Image.open(image).convert('L')

    # Resize the image to match the input size expected by the model (28x28 pixels)
    image = image.resize((28, 28), Image.LANCZOS)

    # Ensure the background is white if transparent
    image = ImageOps.invert(image) if image.getextrema()[-1] == 0 else image

    # Convert the image to a NumPy array and normalize pixel values to [0, 1]
    image = np.array(image) / 255.0

    # Preprocess the image (e.g., invert colors if needed)
    image = preprocess_image(image)

    # Reshape the image to add batch and channel dimensions: (1, 28, 28, 1)
    image = image.reshape(1, 28, 28, 1)

    # Predict the digit using the model
    prediction = model.predict(image)

    # Find the index of the highest probability (the predicted digit)
    predicted_digit = int(np.argmax(prediction))

    return predicted_digit
