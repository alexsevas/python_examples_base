'''
Потоковые компоненты в Gradio

Во время потоковой передачи данные непрерывно отправляются на серверную часть, в
то время как Interface работает непрерывно. У некоторых компонентов, например,
Audio , есть режим потоковой передачи в режиме микрофона, а у компонента Image –
режим веб-камеры.
Во время потоковой передачи требуются дополнительные разрешения для доступа к
звуку и камере в зависимости от типа передачи.
'''

import gradio as gr
import numpy as np

def flip(im):
    return np.flipud(im)

demo = gr.Interface(
    flip,
    gr.Image(source="webcam", streaming=True),
    "image",
    live=True
)

demo.launch()