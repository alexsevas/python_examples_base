# ENV allpy310(2)
from datasets import load_dataset

# Загрузка датасета "imdb" с Hugging Face Hub
dataset = load_dataset("imdb")

print(dataset)
# Вывод: DatasetDict({
#     train: Dataset({
#         features: ['text', 'label'],
#         num_rows: 25000
#     })
#     test: Dataset({
#         features: ['text', 'label'],
#         num_rows: 25000
#     })
#     unsupervised: Dataset({
#         features: ['text', 'label'],
#         num_rows: 50000
#     })
# })

train_data = dataset['train']

print(train_data[0]) #  Доступ к первому примеру в обучающем наборе
# Вывод: {'text': 'A series of escapades demonstrating the adage that what is good for the goose is also good for the gander,
# some of which occasionally amuses but none of which amounts to much of a story.', 'label': 0}



small_train_dataset = dataset["train"].shuffle(seed=42).select(range(1000)) # Перемешивание и выборка


from datasets import ClassLabel
import random
import pandas as pd

def show_random_elements(dataset, num_examples=10):
    picks = []
    n = len(dataset)
    for _ in range(num_examples):
        pick = random.randint(0, n - 1)
        picks.append(dataset[pick])

    df = pd.DataFrame(picks)
    if isinstance(dataset.features['label'], ClassLabel):
        df['label'] = df['label'].apply(lambda x: dataset.features['label'].int2str(x))

    print(df)

show_random_elements(small_train_dataset)
#  Вывод: таблица с 10 случайными примерами


