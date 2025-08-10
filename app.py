import os
import gradio as gr

# TODO: replace these with your real model imports/loader/predict
# Example:
# from foodvision_model.model import load_model, predict

model = None

def load_model():
    # Load and return your trained model here
    return "demo_model"

def predict_image(image):
    # image is a PIL.Image
    # Replace with your real inference code and class mapping
    return "demo_label"

if model is None:
    model = load_model()

demo = gr.Interface(
    fn=predict_image,
    inputs=gr.Image(type="pil", label="Upload food image"),
    outputs=gr.Label(num_top_classes=1, label="Prediction"),
    title="FoodVision (Gradio)",
    description="Upload an image to classify."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", 10000)))
