# **Rainfall Prediction App**

---
![Screenshot 2025-01-27 160808](https://github.com/user-attachments/assets/41317026-b8cd-4905-87ef-086a7eab5f10)

---

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

Welcome to the **Rainfall Prediction App**! This project predicts the **monthly sum of rainfall** based on meteorological data such as Specific Humidity, Relative Humidity, and Temperature. The app is built using **Streamlit** and powered by a **Random Forest Regressor** model trained on data from NASA's POWER project.

🌐 **Live App**: [https://mumbai-rainfall-pred-ak19.onrender.com/](https://mumbai-rainfall-pred-ak19.onrender.com/) 

📂 **GitHub Repository**: [https://github.com/Aakash109-hub/Rainfall_Prediction](https://github.com/Aakash109-hub/Rainfall_Prediction)

---

## **Table of Contents**
1. [Overview](#overview)
2. [Model Details](#model-details)
3. [Dataset](#dataset)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Deployment](#deployment)
7. [Contributing](#contributing)
8. [Acknowledgements](#acknowledgements)

---

## **Overview**
This project aims to predict the **monthly sum of rainfall** using meteorological data. The app takes user inputs for **Specific Humidity**, **Relative Humidity**, and **Temperature** and provides a prediction for the total rainfall expected in a month. The prediction is based on a **Random Forest Regressor** model trained on historical climate data.

---

## **Model Details**
### **Algorithms Tested**
Three machine learning models were evaluated for this project:
1. **Linear Regression**
2. **Random Forest Regressor**
3. **XGBoost Regressor**

### **Model Performance**
| Model                  | RMSE                     | R² Score                 |
|------------------------|--------------------------|--------------------------|
| Linear Regression      | 193.23906389559792       | 0.5901603563614706       |
| Random Forest Regressor| 120.15854738896871       | 0.8415349637940618       |
| XGBoost Regressor      | 154.60391662615186       | 0.7376596467775496       |

The **Random Forest Regressor** was selected as the final model due to its superior performance (lowest RMSE and highest R² score).

### **Features**
- **Specific Humidity** (g/kg)
- **Relative Humidity** (%)
- **Temperature** (°C)

### **Target Variable**
- **Precipitation**: The monthly sum of rainfall (in mm).

---

## **Dataset**
The dataset is sourced from NASA's **Prediction of Worldwide Energy Resources (POWER)** project. It includes monthly meteorological data for Mumbai, India, from **2000 to 2020**. The dataset contains the following variables:
- **Specific Humidity** (g/kg)
- **Relative Humidity** (%)
- **Temperature** (°C)
- **Precipitation** (monthly sum of rainfall in mm)

### **Statistical Summary**
| Feature           | Count  | Mean     | Std      | Min   | 25%    | 50%    | 75%    | Max     |
|-------------------|--------|----------|----------|-------|--------|--------|--------|---------|
| Specific Humidity | 252    | 14.42    | 4.38     | 5.74  | 10.01  | 15.20  | 18.88  | 20.57   |
| Relative Humidity | 252    | 67.26    | 17.31    | 34.69 | 51.85  | 66.66  | 84.61  | 92.31   |
| Temperature       | 252    | 16.32    | 6.58     | 4.73  | 10.87  | 16.92  | 22.12  | 29.34   |
| Precipitation     | 252    | 206.80   | 318.09   | 0.00  | 0.40   | 11.50  | 353.20 | 1307.43 |

---

## **Installation**
To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aakash109-hub/Rainfall_Prediction.git
   cd Rainfall_Prediction
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**
1. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

2. **Input Features**:
   - Enter values for **Specific Humidity**, **Relative Humidity**, and **Temperature** in the sidebar.

3. **Prediction**:
   - Click the **Predict Rainfall** button to get the predicted monthly rainfall.

4. **Output**:
   - The app will display the predicted rainfall in millimeters (mm) along with a visualization and interpretation.

---

## **Deployment**
The app is deployed on **Render** and can be accessed at:  
🌐 [https://mumbai-rainfall-pred-ak19.onrender.com/](https://mumbai-rainfall-pred-ak19.onrender.com/)

### **Steps to Deploy on Render**
1. Push your code to a GitHub repository.
2. Sign up or log in to [Render](https://render.com/).
3. Create a new **Web Service** and connect your GitHub repository.
4. Configure the build and start commands:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py`
5. Deploy the app.

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## **Acknowledgements**
- **NASA POWER Project**: For providing the meteorological data.
- **Streamlit**: For making it easy to build and share web apps.
- **Scikit-Learn**: For providing the machine learning tools.
- **Render**: For hosting the app.
- 
---

Enjoy using the **Rainfall Prediction App**! 🌧️

---

### **Key Updates**
- Added the **Live App** and **GitHub Repository** links at the top.
- Added a **Deployment** section with steps to deploy the app on Render.
- Updated the **Contact** section with your GitHub profile

Let me know if you need further changes! 😊
