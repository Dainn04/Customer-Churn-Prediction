import streamlit as st
import pandas as pd
import numpy as np
from sklearn.externals import joblib  # Nếu sử dụng Scikit-learn
from sklearn.model_selection import train_test_split
import pickle

# Tiêu đề ứng dụng
st.title('Thông tin khách hàng')

# Nhập dữ liệu cho từng trường
gender = st.radio('Gender:', ['Male', 'Female'])
senior_citizen = st.text_input('SeniorCitizen:')
partner = st.radio('Partner:', ['Yes', 'No'])
dependents = st.radio('Dependents:', ['Yes', 'No'])
tenure = st.slider('Tenure:', 0, 100, 12)
phone_service = st.radio('PhoneService:', ['Yes', 'No'])
multiple_lines = st.radio('MultipleLines:', ['Yes', 'No','No phone service'])
internet_service = st.selectbox('InternetService:', ['DSL', 'Fiber optic', 'No'])
online_security = st.radio('OnlineSecurity:', ['Yes', 'No', 'No internet service'])
online_backup = st.radio('OnlineBackup:', ['Yes', 'No', 'No internet service'])
device_protection = st.radio('DeviceProctect:', ['Yes', 'No', 'No internet service'])
tech_support = st.radio('TechSupport:', ['Yes', 'No', 'No internet service '])
streaming_tv = st.radio('StreamingTV:', ['Yes', 'No', 'No internet service'])
streaming_movies = st.radio('StreamingMovies', ['Yes', 'No', 'No internet service'])
contract = st.selectbox('Contract:', ['Month-to-month', 'One year', 'Two year'])
paperless_billing = st.radio('PaperlessBilling:', ['Yes', 'No'])
payment_method = st.selectbox('PaymentMethod:', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly_charges = st.text_input('MonthlyCharges:')
total_charges = st.text_input('TotalCharges:')
predict_button = st.button("Predict")





# Load mô hình đã được huấn luyện
# model =(open("model.sav", 'wb'))  # Thay đổi đường dẫn tới mô hình thực tế

# Xây dựng hàm dự đoán
def predict_churn(gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService,
                   MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
                   DeviceProtection, TechSupport, StreamingTV, StreamingMovies,
                   Contract, PaperlessBilling, PaymentMethod, MonthlyCharges, TotalCharges):
    # Tạo DataFrame từ dữ liệu đầu vào
    input_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [SeniorCitizen],
        'Partner': [Partner],
        'Dependents': [Dependents],
        'tenure': [tenure],
        'PhoneService': [PhoneService],
        'MultipleLines': [MultipleLines],
        'InternetService': [InternetService],
        'OnlineSecurity': [OnlineSecurity],
        'OnlineBackup': [OnlineBackup],
        'DeviceProtection': [DeviceProtection],
        'TechSupport': [TechSupport],
        'StreamingTV': [StreamingTV],
        'StreamingMovies': [StreamingMovies],
        'Contract': [Contract],
        'PaperlessBilling': [PaperlessBilling],
        'PaymentMethod': [PaymentMethod],
        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges],
    })

    # # # Thực hiện dự đoán
    # # prediction = model.predict(input_data)
    #
    # # Trả về kết quả dự đoán (0 hoặc 1)
    # return prediction[0]

# Sử dụng hàm dự đoán
result = predict_churn(gender='Female', SeniorCitizen=0, Partner='Yes', Dependents='No',
                       tenure=10, PhoneService='Yes', MultipleLines='No', InternetService='DSL',
                       OnlineSecurity='No', OnlineBackup='Yes', DeviceProtection='No',
                       TechSupport='No', StreamingTV='No', StreamingMovies='Yes',
                       Contract='Month-to-month', PaperlessBilling='Yes', PaymentMethod='Electronic check',
                       MonthlyCharges=50.0, TotalCharges=500.0)

print("Predicted Churn:", result)




