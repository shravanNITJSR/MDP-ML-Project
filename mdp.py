    # -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:01:27 2024

@author: Shravan 
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#loading the saved modals

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

diabetes_model = pickle.load(open('diabetes_model.sav','rb'))


Breast_cancer_model = pickle.load(open('Breast_Cancer_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Breast Cancer Prediction'],
                           
                           menu_icon='hospital-fill',
                           icons=['capsule', 'chat-left-heart-fill', 'file-person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level [70-100]')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value [70-130]')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value [3-28 mm]')

    with col2:
        Insulin = st.text_input('Insulin Level [5-15] mIUl')

    with col3:
        BMI = st.text_input('BMI(Body Mass index) value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function [0.08-2.42]')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'THE PERSON IS SUFFERING FROM  DIABETES'
        else:
            diab_diagnosis = 'THE PERSON IS NOT SUFFERING FROM  DIABETES'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex [0=Female , 1=Male]')

    with col3:
        cp = st.text_input('Chest Pain types [0-3]')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure  [94-200]')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl [<200]')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar [0=False , 1=Ture]')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results [0=False , 1=Ture]')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved [60-100]')

    with col3:
        exang = st.text_input('Exercise Induced Angina [0=False , 1=Ture]')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise [0-5]')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment [0-2]')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy [0-3]')

    with col1:
        thal = st.text_input('Thal [1-5]')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'THE PERSON IS SUFFERING FROM  HEART DISEASE'
        else:
            heart_diagnosis = 'THE PERSON IS NOT SUFFERING FROM  HEART DISEASE'

    st.success(heart_diagnosis)


# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':

    # page title    
    st.title('Breast Cancer Prediction')

    col1, col2, col3 = st.columns(3)    

    with col1:
        meanradius = st.text_input('Mean Radius')

    with col2:
        meantexture = st.text_input('Mean Texture')

    with col3:
        meanperimeter= st.text_input('Mean Perimeter')

    with col1:
        meanarea = st.text_input('Mean Area')

    with col2:
        meansmoothness = st.text_input('Mean Smoothness')

    with col3:
        meancompactness = st.text_input('Mean Compactness')

    with col1:
        meanconcavity = st.text_input('Mean Concavity')

    with col2:
        meanconcavepoints = st.text_input('Mean Concave Points')

    with col3:
        meansymmetry = st.text_input('Mean Symmetry')

    with col1:
        meanfractaldimension = st.text_input('Mean Fractal Dimension')

    with col2:
        radiuserror = st.text_input('Radius Error')

    with col3:
        textureerror = st.text_input('Texture Error')            
    
    with col1:
        perimetererror = st.text_input('Perimeter Error')

    with col2:
        areaerror = st.text_input('Area Error')

    with col3:
        smoothnesserror = st.text_input('Smoothness Error')
   
    with col1:
        compactnesserror = st.text_input('Compactness Error')

    with col2:
        concavityerror = st.text_input('Concavity Error')

    with col3:
        concavepointserror = st.text_input('Concave Points Error')     
        
    with col1:
        symmetryerror= st.text_input('Symmetry Error')

    with col2:
        fractaldimensionerror = st.text_input('Fractal Dimension Error')

    with col3:
        worstradius = st.text_input('Worst Radius')
        
    with col1:
        worsttexture = st.text_input(' Worst Texture')

    with col2:
        worstperimeter = st.text_input('Worst Perimeter')

    with col3:
        worstarea = st.text_input(' Worst Area')
        
    with col1:
        worstsmoothness = st.text_input(' Worst Smoothness')

    with col2:
        worstcompactness = st.text_input(' Worst Compactness')

    with col3:
        worstconcavity = st.text_input('Worst Concavity')
        
    with col1:
        worstconcavepoints = st.text_input('  Worst Concave Points')

    with col2:
        worstsymmetry = st.text_input('Worst Symmetry')

    with col3:
        worstfractaldimension = st.text_input(' Worst Fractal Dimension')
    # code for Prediction
    breast_diagnosis = ''

    # creating a button for Prediction

    if st.button('Breast Cancer Test Result'):
        user_input = [meanradius, meantexture, meanperimeter, meanarea, meansmoothness, meancompactness,
                      meanconcavity, meanconcavepoints, meansymmetry, meanfractaldimension, radiuserror,
                      textureerror, perimetererror, areaerror, smoothnesserror, compactnesserror, concavityerror, 
                      concavepointserror, symmetryerror,fractaldimensionerror, worstradius, worsttexture,
                      worstperimeter,worstarea, worstsmoothness, worstcompactness, worstconcavity,worstconcavepoints,
                      worstsymmetry, worstfractaldimension] 

        user_input = [float(x) for x in user_input]

        breast_diagnosis = Breast_cancer_model.predict([user_input])

        if breast_diagnosis[0] == 1:
            breast_diagnosis = 'THE PERSON IS SUFFERING FROM BREAST CANCER'
        else:
            breast_diagnosis = 'THE PERSON IS NOT SUFFERING FROM BREAST CANCER'

    st.success(breast_diagnosis)
