import gradio as gr
import requests

URL = "https://oyntw3ljhg.execute-api.us-east-1.amazonaws.com/test/hg-func-resource"

def output(inputs):
    r = requests.post(url=URL, json={"inputs": inputs}).content
    return r

demo = gr.Interface(
    fn=output,
    inputs=["text"],
    outputs=["text"]
)

demo.launch()