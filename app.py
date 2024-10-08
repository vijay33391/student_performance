import streamlit as st
from src.pipelines.predect_pipeline import CustomData,PredictPipeline

# Streamlit App Interface
st.title("Math Score Prediction")

st.write("""
This application predicts a student's Math score based on various factors such as gender, race/ethnicity, parental education, lunch type, test preparation, and other scores.
""")

# Function to get user input
def get_user_input():
    gender = st.selectbox("Select Gender", ["female", "male"])
    race_ethnicity = st.selectbox("Race/Ethnicity", 
                                   ["group B", "group C", "group A", "group D", "group E"])
    parental_level_of_education = st.selectbox("Parental Level of Education", 
                                                ["high school", "some college", "associate's degree", 
                                                 "bachelor's degree", "master's degree", "some high school"])
    lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
    test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
    reading_score = st.slider("Reading Score", 0, 100, 69)
    writing_score = st.slider("Writing Score", 0, 100, 68)
    
    return CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

# Store the user input in session state
if 'user_input' not in st.session_state:
    st.session_state.user_input = None

# Get user input when the app runs
user_input = get_user_input()

# Display the input data
if user_input:
    st.write("Input Data:")
    st.dataframe(user_input.get_data_as_data_frame())

# Predict Button
if st.button('Predict'):
    if user_input is not None:
        try:
            # Convert user input to DataFrame
            pred_df = user_input.get_data_as_data_frame()

            # Make predictions using the PredictPipeline class
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            
            # Display prediction result
            st.success(f"Predicted Math Score: {results[0]}")
        
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide input data before predicting.")

# Add a reset button to clear the session state if needed
if st.button("Reset"):
    st.session_state.user_input = None
    st.success("Inputs reset.")
