#!/usr/bin/env python
# coding: utf-8

# ![APP%20Heart%20diseases%20%281%29.jpg](attachment:APP%20Heart%20diseases%20%281%29.jpg)

# In[1]:


import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# In[2]:


# Загрузка модели машинного обучения
@st.cache
def load_model():
    model = joblib.load('https://github.com/AniMilina/APP-Heart-diseases/blob/main/model_dump.mdl')
    return model


# In[3]:


# Заголовок приложения
st.title('Определение риска возникновения сердечно-сосудистых заболеваний')

# Создание боковой панели с настройками
with st.sidebar:
    age = st.slider('Возраст', min_value=1, max_value=100, value=50)
    gender = st.selectbox('Пол', ['Мужской', 'Женский'])
    bmi = st.slider('ИМТ', min_value=10, max_value=50, value=55)
    height = st.slider('Рост, см', min_value=100, max_value=250, value=170)
    weight = st.slider('Вес, кг', min_value=30, max_value=200, value=70)
    systolic_bp = st.slider('Систолическое АД, мм рт. ст.', min_value=80, max_value=240, value=120)
    diastolic_bp = st.slider('Диастолическое АД, мм рт. ст.', min_value=40, max_value=140, value=80)
    cholesterol = st.selectbox('Уровень холестерина', ['Норма', 'Высокий'])
    glucose = st.selectbox('Уровень глюкозы', ['Норма', 'Высокий'])

# Создание кнопки для запуска анализа
if st.button('Рассчитать риск'):
    # Загрузка модели машинного обучения
    model = load_model()

    # Преобразование категориальных признаков в числовые
    gender_enc = LabelEncoder().fit_transform([gender])
    cholesterol_enc = LabelEncoder().fit_transform([cholesterol])
    glucose_enc = LabelEncoder().fit_transform([glucose])

    # Создание датафрейма из входных данных
    input_data = pd.DataFrame({
        'age': [age],
        'gender': gender_enc,
        'bmi': [bmi],
        'height': [height],
        'weight': [weight],
        'systolic_bp': [systolic_bp],
        'diastolic_bp': [diastolic_bp],
        'cholesterol': cholesterol_enc,
        'glucose': glucose_enc
    })

    # Анализ данных и вывод результата
    result = model.predict_proba(input_data)[:, 1][0]
    st.write('Риск возникновения сердечно-сосудистых заболеваний:', round(result * 100, 2), '%')


# In[ ]:





# In[ ]:





# In[ ]:




