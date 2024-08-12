import gradio as gr
from utils import predict_digit

interface = gr.Interface(
    fn=predict_digit,  # The function that takes input and returns output
    inputs=gr.Image(),  # Grayscale image
    outputs=gr.Label(),  # Display prediction label
    live=True  # Allow live updating as the user draws
)
interface.launch()



