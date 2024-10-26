# conda activate allpy310

from transformers import pipeline

pipe = pipeline("text-classification")
result = pipe("Good day!")

print(result)

#[{'label': 'POSITIVE', 'score': 0.9998743534088135}]