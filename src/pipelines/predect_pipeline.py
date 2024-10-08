import os
import sys
import pandas as pd
from src.utils import load_object
from src.exception import CustomException
from src.logger import logging

class PredictPipeline:
    def __init__(self):
        logging.info("PredictPipeline instance created")

    def predict(self, features):
        logging.info("Starting the prediction process")
        try:
            # Load the model and preprocessor
            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            
            # Load the model and preprocessor objects
            logging.info(f"Loading model from {model_path} and preprocessor from {preprocessor_path}")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            
            # Scale and transform the input features
            data_scaled = preprocessor.transform(features)
            logging.info("Input features scaled and transformed")
            
            # Predict the math score
            preds = model.predict(data_scaled)
            logging.info("Prediction made successfully")

            return preds
        
        except Exception as e:
            logging.error(f"Error occurred during prediction: {str(e)}")
            raise CustomException(f"Prediction failed: {str(e)}", sys)

class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score):
        logging.info("CustomData instance created with input features")

        # Define valid values for categorical features
        valid_genders = ['female', 'male']
        valid_race_ethnicity = ['group A', 'group B', 'group C', 'group D', 'group E']
        valid_parental_level_of_education = [
            "bachelor's degree", 'some college', 
            "master's degree", "associate's degree", 
            'high school', 'some high school'
        ]
        valid_lunch = ['standard', 'free/reduced']
        valid_test_preparation_course = ['none', 'completed']

        # Validate input features
        if gender not in valid_genders:
            raise ValueError(f"Invalid gender: {gender}. Valid options are {valid_genders}.")
        if race_ethnicity not in valid_race_ethnicity:
            raise ValueError(f"Invalid race/ethnicity: {race_ethnicity}. Valid options are {valid_race_ethnicity}.")
        if parental_level_of_education not in valid_parental_level_of_education:
            raise ValueError(f"Invalid parental level of education: {parental_level_of_education}. Valid options are {valid_parental_level_of_education}.")
        if lunch not in valid_lunch:
            raise ValueError(f"Invalid lunch type: {lunch}. Valid options are {valid_lunch}.")
        if test_preparation_course not in valid_test_preparation_course:
            raise ValueError(f"Invalid test preparation course: {test_preparation_course}. Valid options are {valid_test_preparation_course}.")

        # Assign validated inputs to instance variables
        self.gender = gender
        self.race_ethnicity = race_ethnicity  # Keep original case
        self.parental_level_of_education = parental_level_of_education  # Keep original case
        self.lunch = lunch  # Keep original case
        self.test_preparation_course = test_preparation_course  # Keep original case
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        logging.info("Converting input data to DataFrame")
        try:
            # Prepare the data as a dictionary for DataFrame conversion
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("DataFrame created successfully")
            return df
        
        except Exception as e:
            logging.error(f"Error occurred while creating DataFrame: {str(e)}")
            raise CustomException(f"DataFrame creation failed: {str(e)}", sys)
