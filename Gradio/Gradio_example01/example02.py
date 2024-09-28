'''
Отображение текста в Gradio
Текст можно отобразить с помощью gradio.Text или gradio.Textbox . Каждый
метод предоставляет область для ввода строкового ввода или отображения строкового
вывода
'''

#display a text
import gradio as gr
def text_display(text):
    return text

demo = gr.Interface(text_display, gr.Text(), "text")
#alternatively use gr.TextBox()
demo.launch()