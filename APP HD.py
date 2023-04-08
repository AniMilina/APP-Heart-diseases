#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pickle
import tkinter as tk

with open('C:\\Users\\Admin\\Desktop\\DS studies\\Data\\Heart diseases\\PROJECT\\FINAL\\model_dump.mdl', 'rb') as f:
    model = pickle.load(f)


# In[12]:


def predict_cardio_risk(age, gender, bmi, systolic_bp, cholesterol, glucose, smoking):
    """
    Predicts the risk of cardiovascular disease given patient information.
    
    Args:
    - age (int): age of patient
    - gender (str): gender of patient ('male' or 'female')
    - bmi (int): body mass index
    - systolic_bp (int): systolic blood pressure of patient
    - cholesterol (int): total cholesterol of patient
    - glucose (int): fasting blood glucose of patient
    - smoking (str): whether or not patient smokes ('yes' or 'no')
    
    Returns:
    - risk (str): predicted risk of cardiovascular disease ('low', 'medium', or 'high')
    """
    # Process input / процесс ввода данных:
    if gender.lower() == 'male':
        gender = 1
    elif gender.lower() == 'female':
        gender = 0
    else:
        raise ValueError("Gender must be 'male' or 'female'.")
        
    if smoking.lower() == 'yes':
        smoking = 1
    elif smoking.lower() == 'no':
        smoking = 0
    else:
        raise ValueError("Smoking must be 'yes' or 'no'.")
    
    # Create input array / Создаём массив:
    input_array = [[age, gender, bmi, systolic_bp, cholesterol, glucose, smoking]]
    
    # Make prediction / Сделаем прогноз:
    risk = model.predict(input_array)[0]
    
    # Interpret prediction / Интерпретируем предсказание: 
    if risk == 0:
        return 'low'
    elif risk == 1:
        return 'medium'
    else:
        return 'high'


# In[13]:


# Create main window / Создаём главное окно:
root = tk.Tk()
root.title('Cardiovascular Risk Predictor')

# Create input labels and entry widgets / Создём метки ввода и виджетов:
age_label = tk.Label(root, text='Age:')
age_entry = tk.Entry(root)

gender_label = tk.Label(root, text='Gender:')
gender_entry = tk.Entry(root)

bmi_label = tk.Label(root, text='BMI:')
bmi_entry = tk.Entry(root)

bp_label = tk.Label(root, text='Systolic Blood Pressure:')
bp_entry = tk.Entry(root)

cholesterol_label = tk.Label(root, text='Total Cholesterol:')
cholesterol_entry = tk.Entry(root)

glucose_label = tk.Label(root, text='Fasting Blood Glucose:')
glucose_entry = tk.Entry(root)

smoking_label = tk.Label(root, text='Smoking:')
smoking_entry = tk.Entry(root)

# Add input labels and entry widgets to window / Добавим метки ввода и виджеты в окно:
age_label.pack()
age_entry.pack()

gender_label.pack()
gender_entry.pack()

bmi_label.pack()
bmi_entry.pack()

bp_label.pack()
bp_entry.pack()

cholesterol_label.pack()
cholesterol_entry.pack()

glucose_label.pack()
glucose_entry.pack()

smoking_label.pack()
smoking_entry.pack()

# Create function to handle button click / Функция для обработки нажатия кнопки:
def predict():
    age = int(age_entry.get())
    gender = gender_entry.get()
    bmi = int(bmi_entry.pack())
    bp = int(bp_entry.get())
    cholesterol = int(cholesterol_entry.get())
    glucose = int(glucose_entry.get())
    smoking = smoking_entry.get()
    
    risk = predict_cardio_risk(age, gender, bmi, bp, cholesterol, glucose, smoking)
    
    result_label.config(text=f'Predicted risk: {risk}')

# Create button to make prediction / Создадим кнопку, чтобы сделать прогноз:
predict_button = tk.Button(root, text='Predict Risk', command=predict)
predict_button.pack()

# Create label to display result / Создадим метку для отображения результата:
result_label = tk.Label(root)
result_label.pack()

# Start the main event loop / Запустим цикл:
root.mainloop()

