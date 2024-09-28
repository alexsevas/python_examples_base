'''
Отображение мультимедиа в Gradio
Вы можете отображать медиафайлы, например, изображения, в Gradio. Кроме того, вы
можете преобразовывать изображения с помощью фильтров, например, сепия или
фильтр синего оттенка. Чтобы вывести на экран различные типы мультимедиа, нужно
передать в качестве входных данных Image , Video , Audio или File .
В приведенном ниже примере показано, как визуализировать изображение после
применения фильтра синего оттенка.
'''

import numpy as np
import gradio as gr
def blue_hue(input_img):
    blue_hue_filter = np.array([
        [0.272, 0.534, 0.131],
        [0.349, 0.686, 0.168],
        [0.393, 0.769, 0.189]])
    blue_hue_img = input_img.dot(blue_hue_filter.T)
    blue_hue_img /= blue_hue_img.max()
    return blue_hue_img

demo = gr.Interface(blue_hue, gr.Image(shape=(300, 200)), "image")
demo.launch()