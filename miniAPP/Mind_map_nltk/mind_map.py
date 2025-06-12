# conda activate allpy310

'''
Генерация Mind Map (интеллект-карты) из текста или речи (локально).
Где применимо:
- Учёба: быстро “увидеть” структуру темы
- Анализ видео, книг, уроков
- Самообразование — делать себе шпаргалки
- Создание презентаций и материалов для других
'''


import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import string

TEXT = """
Look in thy glass and tell the face thou viewest
Now is the time that face should form another;
Whose fresh repair if now thou not renewest,
Thou dost beguile the world, unbless some mother.
For where is she so fair whose uneared womb
Disdains the tillage of thy husbandry?
Or who is he so fond will be the tomb
Of his self-love, to stop posterity?
"""

def extract_keywords(text):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    words = [w for w in words if w.isalnum() and w not in stop_words]
    freq = defaultdict(int)
    for w in words:
        freq[w] += 1
    return sorted(freq.items(), key=lambda x: -x[1])[:10]

def build_mind_map(text):
    keywords = [kw for kw, _ in extract_keywords(text)]
    sentences = sent_tokenize(text)
    G = nx.Graph()

    G.add_node("Main Idea")

    for kw in keywords:
        G.add_node(kw)
        G.add_edge("Main Idea", kw)

        for s in sentences:
            if kw in s.lower():
                for sub_kw in word_tokenize(s.lower()):
                    if sub_kw not in keywords and sub_kw.isalnum():
                        G.add_node(sub_kw)
                        G.add_edge(kw, sub_kw)

    return G

def draw_mind_map(G):
    pos = nx.spring_layout(G, k=0.6)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000, font_size=10, edge_color="gray")
    plt.title("🧠 Mind Map", fontsize=20)
    plt.savefig("mind_map.png")
    print("✅ Карта сохранена в mind_map.png")

G = build_mind_map(TEXT)
draw_mind_map(G)
