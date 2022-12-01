import gradio as gr
import requests

URL = "https://oyntw3ljhg.execute-api.us-east-1.amazonaws.com/test/hg-func-resource"

def output(inputs):
    r = requests.post(url=URL, json={"inputs": inputs}).content
    return r

with gr.Blocks() as demo:
    gr.Markdown("Classify Text or FAQ")
    with gr.Tab("Classification"):
        classification_input = gr.Textbox(label="Input")
        classification_output = gr.Textbox(label="Output")
        classification_button = gr.Button("Classify")
    with gr.Tab("FAQ"):
        faq_input = gr.Textbox(label="Input")
        faq_output = gr.Textbox(label="Output")
        faq_button = gr.Button("Get FAQ")

    classification_button.click(
        output, 
        inputs=classification_input, 
        outputs=classification_output)
    faq_button.click(
        output,
        inputs=faq_input,
        outputs=faq_output
    )

demo.launch()