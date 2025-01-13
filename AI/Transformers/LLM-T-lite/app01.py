from transformers import AutoTokenizer, AutoModelForCausalLM    #, AutoModelForSeq2SeqLM
import torch
import os

'''
# Загрузка токенизатора и модели
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large")
'''

torch.manual_seed(42)

os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

model_name = "t-bank-ai/T-lite-instruct-0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

messages = [
    {"role": "user", "content": "Напиши рецепт классной пиццы!"},
]

input_ids = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

terminators = [
    tokenizer.eos_token_id,
    tokenizer.convert_tokens_to_ids("<|eot_id|>")
]

outputs = model.generate(
    input_ids,
    max_new_tokens=256,
    eos_token_id=terminators,
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))