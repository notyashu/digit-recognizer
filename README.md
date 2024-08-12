# Digit Recognizer

This repository contains the code and resources for a Convolutional Neural Network (CNN) based digit recognition model. The model is trained to recognize handwritten digits (0-9) using a dataset from Kaggle's Digit Recognizer competition. The repository also includes a Gradio-based web interface that allows users to interact with the model by drawing digits on a canvas and getting live predictions.

## Project Overview

The Digit Recognizer project utilizes a Convolutional Neural Network (CNN) implemented with TensorFlow to classify handwritten digits. The model is trained on a dataset of grayscale images of digits and is capable of accurately predicting the digit displayed in a given image.

The project also includes a Gradio-based user interface where users can draw digits and receive instant predictions from the model. The interface is live and updates predictions in real-time as the user draws.

## Dependencies

The project requires the following Python libraries:

* `tensorflow`
* `gradio`

These dependencies are listed in the `requirements.txt` file and can be installed using pip.

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/YOUR_USERNAME/digit-recognizer.git
   cd digit-recognizer
   ```

2. **Create a Virtual Environment** (Optional but recommended):

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Gradio App**:

   ```bash
   python app.py
   ```

   This will start the Gradio interface, which you can access through your web browser.

## Usage

After setting up the environment, you can interact with the digit recognition model through the Gradio interface. Simply draw a digit on the canvas, and the model will display its prediction in real-time.

The model can also be tested with sample images provided in the `Sample Images` directory.

## Model Deployment

The trained model is also deployed on Hugging Face Spaces, allowing users to interact with the model online without setting up the environment locally. You can access the live model here:

[Digit Recognizer on Hugging Face](https://huggingface.co/spaces/notyashu/digit-recognizer)

## Contributing

Contributions to this project are welcome. If you have ideas for improvements or new features, feel free to fork the repository and submit a pull request. Please ensure that your code adheres to the existing style and includes appropriate tests.
