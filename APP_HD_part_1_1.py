#!/usr/bin/env python
# coding: utf-8

# In[28]:


import pickle
import tkinter as tk

# Load model
with open('C:\\Users\\Admin\\Desktop\\DS studies\\Data\\Heart diseases\\PROJECT\\FINAL\\model_dump.mdl', 'rb') as f:
    model = pickle.load(f)


# In[29]:


def predict_cardio_risk():
    """
    Predicts the risk of cardiovascular disease given patient information.
    
    """
    # Get input values from user
    age = age_entry.get()
    gender = gender_var.get()
    bmi = bmi_entry.get()
    systolic_bp = bp_entry.get()
    cholesterol = chol_entry.get()
    glucose = glu_entry.get()
    smoking = smoking_var.get()

    # Process input
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
    
    # Create input array
    input_array = [[age, gender, bmi, systolic_bp, cholesterol, glucose, smoking]]
    
    # Make prediction
    risk = model.predict(input_array)[0]
    
    # Interpret prediction
    if risk == 0:
        return 'low'
    elif risk == 1:
        return 'medium'
    else:
        return 'high'
    


# In[30]:


def submit_data():
    """
    Validates user input and, if valid, calls predict_cardio_risk function to get risk prediction.
    
    """
    # Validate input
    if not age_entry.get().isdigit():
        messagebox.showerror('Error', 'Age must be a number.')
        return
    if not bmi_entry.get().replace('.', '', 1).isdigit():
        messagebox.showerror('Error', 'BMI must be a number.')
        return
    if not bp_entry.get().isdigit():
        messagebox.showerror('Error', 'Systolic BP must be a number.')
        return
    if not chol_entry.get().isdigit():
        messagebox.showerror('Error', 'Total cholesterol must be a number.')
        return
    if not glu_entry.get().isdigit():
        messagebox.showerror('Error', 'Fasting blood glucose must be a number.')
        return
    
    # Call predict_cardio_risk function
    risk = predict_cardio_risk()
    
    # Display result
    result_label.config(text=f'Predicted risk: {risk}')


# In[31]:


#  # Create input array
# input_array = [[age, gender, bmi, systolic_bp, cholesterol, glucose, smoking]]
    
#     # Make prediction
# risk = model.predict(input_array)[0]
    
#     # Interpret prediction
# if risk == 0:
#     return 'low'
# elif risk == 1:
#     return 'medium'
# else:
#     return 'high'


# In[32]:


# Create main window
root = tk.Tk()
root.title('Cardiovascular Risk Predictor')

# Create input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# In[33]:


# Create input labels and entry widgets
age_label = tk.Label(input_frame, text='Age:', font=('Arial', 12))
age_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
age_entry = tk.Entry(input_frame, font=('Arial', 12))
age_entry.grid(row=0, column=1, padx=5, pady=5)

gender_label = tk.Label(input_frame, text='Gender:', font=('Arial', 12))
gender_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
gender_entry = tk.Entry(input_frame, font=('Arial', 12))
gender_entry.grid(row=1, column=1, padx=5, pady=5)

bmi_label = tk.Label(input_frame, text='BMI:', font=('Arial', 12))
bmi_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
bmi_entry = tk.Entry(input_frame, font=('Arial', 12))
bmi_entry.grid(row=2, column=1, padx=5, pady=5)

bp_label = tk.Label(input_frame, text='Systolic Blood Pressure:', font=('Arial', 12))
bp_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
bp_entry = tk.Entry(input_frame, font=('Arial', 12))
bp_entry.grid(row=3, column=1, padx=5, pady=5)  
              
cholesterol_label = tk.Label(input_frame, text='Сholesterol:', font=('Arial', 12))
cholesterol_label.grid(row=4, column=0, padx=5, pady=5, sticky='w')
cholesterol_entry = tk.Entry(input_frame, font=('Arial', 12))
cholesterol_entry.grid(row=4, column=1, padx=5, pady=5)   
                       
glucose_label = tk.Label(input_frame, text='Glucose:', font=('Arial', 12))
glucose_label.grid(row=5, column=0, padx=5, pady=5, sticky='w')
glucose_entry = tk.Entry(input_frame, font=('Arial', 12))
glucose_entry.grid(row=5, column=1, padx=5, pady=5) 
                   

smoking_label = tk.Label(input_frame, text='Smoking:', font=('Arial', 12))
smoking_label.grid(row=6, column=0, padx=5, pady=5, sticky='w')
smoking_entry = tk.Entry(input_frame, font=('Arial', 12))
smoking_entry.grid(row=6, column=1, padx=5, pady=5) 


# In[34]:


# Create input labels and entry widgets
age_label = tk.Label(input_frame, text='Age:', font=('Arial', 12),
                     anchor='w', width=20)
age_entry = tk.Entry(input_frame, font=('Arial', 12), width=20)

gender_label = tk.Label(input_frame, text='Gender:', font=('Arial', 12),
                        anchor='w', width=20)
gender_entry = tk.Entry(input_frame, font=('Arial', 12), width=20)

bmi_label = tk.Label(input_frame, text='BMI:', font=('Arial', 12),
                     anchor='w', width=20)
bmi_entry = tk.Entry(input_frame, font=('Arial', 12), width=20)

bp_label = tk.Label(input_frame, text='Systolic Blood Pressure:', font=('Arial', 12),
                    anchor='w', width=20)
bp_entry = tk.Entry(input_frame, font=('Arial', 12), width=20)

cholesterol_label = tk.Label(input_frame, text='Total Cholesterol:', font=('Arial', 12),
                             anchor='w', width=20)
cholesterol_entry = tk.Entry(input_frame, font=('Arial', 12), width=20)

glucose_label = tk.Label(input_frame, text='Fasting Blood Glucose:', font=('Arial', 12),
                         anchor='w', width=20)
glucose_entry = tk.Entry(input_frame, font=('Arial', 12), width=20)

smoking_label = tk.Label(input_frame, text='Smoking:', font=('Arial', 12),
                         anchor='w', width=20)
smoking_entry = tk.Entry(input_frame, font=('Arial', 12), width=20)


# In[35]:


# Create predict button
predict_button = tk.Button(root, text='Predict Risk', font=('Arial', 12),
                           command=predict_cardio_risk)

# Create label to display result
result_label = tk.Label(root, text='', font=('Arial', 12), width=40, anchor='w')


# In[36]:


# Add input frame and predict button to main window
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky='w')
predict_button.grid(row=1, column=0, padx=10, pady=10)

# Add result label to main window
result_label.grid(row=2, column=0, padx=10, pady=10, sticky='w')


# In[ ]:




