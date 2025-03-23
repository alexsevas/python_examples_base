# conda activate allpy310
# Запуск скрипта командой:
# streamlit run C:\PROJECTS\BASE\GUI_WEB_interface\streamlit\streamlit_example01.py --server.port 8504

import streamlit as st
import pandas as pd
import numpy as np

# Заголовок приложения
st.title('Пример приложения Streamlit')

# Ввод числа пользователем
number = st.number_input('Введите число', min_value=0, max_value=100, value=50)

# Показываем текст в зависимости от введенного числа
st.write(f'Ваше число: {number}')

# Создаем случайные данные и строим график
data = pd.DataFrame({
  'x': range(1, 101),
  'y': np.random.randn(100).cumsum()
})
st.line_chart(data)
