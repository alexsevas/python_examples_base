'''
Отображение кода в Gradio
Используйте gradio.Textbox для отображения кода.
'''

import gradio as gr
#define your code
#average of a list
code = '''def cal_average(numbers):
sum_number = 0
for t in numbers:
sum_number = sum_number + t
average = sum_number / len(numbers)
return average'''
with gr.Blocks() as demo:
    gr.Textbox(code)
demo.launch()