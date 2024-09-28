#conda activate allpy310
#ENV allpy310, allpy39

# pip install gradio

'''import gradio as gra
def user_greeting(name):
    return "Hi! " + name + " Welcome to Gradio!"

#define gradio interface
app = gra.interface(fn=user_greeting, inputs ="Text", outputs = "Text")
app.launch()'''

#!pip install gradio
import gradio as gra
def user_greeting(name):
    return "Hi! " + name + " Welcome to your first Gradio application!😎"
#define gradio interface and other parameters
app = gra.Interface(fn = user_greeting, inputs="text", outputs="text")
app.launch()

