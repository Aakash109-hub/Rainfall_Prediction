import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the model (ensure this is the path where the model is saved)
try:
    with open('random_forest.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'random_forest.pkl' is in the correct directory.")
    st.stop()

# Streamlit App UI
st.title("🌧️ Monthly Rainfall Prediction App")
st.markdown("""
    Welcome to the **Monthly Rainfall Prediction App**!  
    This app predicts the **total monthly rainfall** (in mm) based on meteorological data such as Specific Humidity, Relative Humidity, and Temperature.  
    The data is sourced from NASA's POWER project, which provides long-term climate estimates for renewable energy and agricultural support.
""")

# Sidebar for user input
st.sidebar.header("User Input Features")
st.sidebar.markdown("Enter the meteorological data below to predict monthly rainfall:")

specific_humidity = st.sidebar.number_input('Specific Humidity (g/kg)', min_value=0.0, value=14.42)
relative_humidity = st.sidebar.number_input('Relative Humidity (%)', min_value=0.0, max_value=100.0, value=67.26)
temperature = st.sidebar.number_input('Temperature (°C)', min_value=-50.0, max_value=50.0, value=16.32)

# Prepare input data for prediction
input_data = pd.DataFrame({
    'Specific Humidity': [specific_humidity],
    'Relative Humidity': [relative_humidity],
    'Temperature': [temperature]
})

# Make prediction
if st.sidebar.button('Predict Monthly Rainfall'):
    try:
        prediction = model.predict(input_data)
        monthly_rainfall = prediction[0]

        # Display prediction result
        st.subheader("Prediction Result")
        st.markdown(f"**Predicted Monthly Rainfall:** {monthly_rainfall:.2f} mm")

        # Visualize the prediction
        st.markdown("### 📊 Monthly Rainfall Visualization")
        fig, ax = plt.subplots()
        ax.bar(['Monthly Rainfall'], [monthly_rainfall], color='skyblue')
        ax.set_ylabel('Rainfall (mm)')
        ax.set_title('Predicted Monthly Rainfall')
        st.pyplot(fig)

        # Add a description based on monthly rainfall level
        st.markdown("### 🌧️ Rainfall Interpretation")
        if monthly_rainfall < 50:
            st.info("**Low Rainfall**: This month is expected to be relatively dry. Suitable for outdoor activities.")
        elif 50 <= monthly_rainfall < 200:
            st.warning("**Moderate Rainfall**: Expect moderate rainfall this month. Plan accordingly for agricultural or outdoor activities.")
        else:
            st.error("**High Rainfall**: This month is expected to have heavy rainfall. Be prepared for potential flooding or waterlogging.")

        # Add statistical insights
        st.markdown("### 📈 Statistical Insights")
        st.markdown("Here are some key statistics from the historical dataset:")
        st.write("""
            - **Mean Monthly Rainfall**: 206.80 mm
            - **Minimum Monthly Rainfall**: 0.00 mm
            - **Maximum Monthly Rainfall**: 1307.43 mm
            - **25th Percentile**: 0.40 mm
            - **50th Percentile (Median)**: 11.50 mm
            - **75th Percentile**: 353.20 mm
        """)

        # Compare prediction with historical data
        st.markdown("### 🔍 Comparison with Historical Data")
        if monthly_rainfall < 11.50:
            st.info("The predicted rainfall is **below the median** historical monthly rainfall.")
        elif 11.50 <= monthly_rainfall < 353.20:
            st.warning("The predicted rainfall is **within the interquartile range** of historical monthly rainfall.")
        else:
            st.error("The predicted rainfall is **above the 75th percentile** of historical monthly rainfall.")

        # Add a fun fact about rainfall
        st.markdown("### 💡 Did You Know?")
        st.markdown("""
            - **100 mm of rainfall** over 1 square meter is equivalent to **100 liters of water**.
            - Mumbai, India, receives an average of **2422 mm of rainfall annually**, mostly during the monsoon season.
        """)

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

# Add a footer
st.markdown("---")
st.markdown("""
    **Data Source**: NASA's POWER Project  
    **Model**: Random Forest Regressor  
    **Developed by**: Aakash Gayke  
    For more information, visit [NASA POWER](https://power.larc.nasa.gov/).
""")