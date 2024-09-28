'''
Отображение данных в Gradio
Такие типы данных, как «str», «number», «bool», «date» и «markdown», могут отображаться
в Gradio. По умолчанию вы получите Pandas DataFrame.
Вы можете получить другие типы данных, указав желаемый тип вывода. Например,
массив NumPy может быть получен при указании numpy , а array – для массива
Python.
'''

#display a data
import gradio as gr
def data_display(input_img):
    return input_img
demo = gr.Interface(data_display, gr.Dataframe(), "dataframe")
demo.launch()