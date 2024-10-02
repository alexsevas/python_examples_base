from transformers import pipeline

pipe = pipeline("text-classification")
result = pipe("This restaurant is awesome")

print(result)

#[{'label': 'POSITIVE', 'score': 0.9998743534088135}]