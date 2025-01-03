## README

### Project Title: Math Score Prediction

### Description
This project is designed to predict a student's Math score based on various factors such as gender, race/ethnicity, parental education, lunch type, test preparation, and other scores. The application uses a user-friendly interface to input these variables and provides a predicted Math score.

### LIVE DEMO
CHECK OUT HERE:[LIVE DEMO](https://studentperformance-g8qoohgfvzmetpfjylgnkd.streamlit.app/)

### Features
- **Gender Selection**: Allows the user to select the gender of the student.
- **Race/Ethnicity Selection**: Allows the user to select the race/ethnicity group of the student.
- **Parental Level of Education**: Allows the user to select the highest level of education attained by the student's parents.
- **Lunch Type**: Allows the user to select the type of lunch the student receives (standard or free/reduced).
- **Test Preparation Course**: Allows the user to select whether the student has completed a test preparation course.
- **Reading Score Input**: Allows the user to input the student's reading score (0-100).
- **Writing Score Input**: Allows the user to input the student's writing score (0-100).
- **Prediction Output**: Displays the predicted Math score based on the input data.

### How to Use
1. **Select Gender**: Choose the gender of the student from the dropdown menu.
2. **Select Race/Ethnicity**: Choose the race/ethnicity group of the student from the dropdown menu.
3. **Select Parental Level of Education**: Choose the highest level of education attained by the student's parents from the dropdown menu.
4. **Select Lunch Type**: Choose the type of lunch the student receives from the dropdown menu.
5. **Select Test Preparation Course**: Choose whether the student has completed a test preparation course from the dropdown menu.
6. **Input Reading Score**: Use the slider to input the student's reading score (0-100).
7. **Input Writing Score**: Use the slider to input the student's writing score (0-100).
8. **Predict**: Click the "Predict" button to get the predicted Math score.
9. **Reset**: Click the "Reset" button to clear all inputs.

### Example
- **Gender**: Female
- **Race/Ethnicity**: Group B
- **Parental Level of Education**: High School
- **Lunch Type**: Standard
- **Test Preparation Course**: Completed
- **Reading Score**: 69
- **Writing Score**: 68

### Input Data Table
| Index | Parental Level of Education | Lunch | Test Preparation Course | Reading Score | Writing Score |
|-------|-----------------------------|-------|-------------------------|---------------|---------------|
| 0     | High School                 | Standard| Completed              | 69            | 68            |

### Notes
- Ensure all inputs are correctly filled before clicking the "Predict" button.
- The "Reset" button will clear all the inputs, allowing for a new prediction.

### Dependencies
- numpy
- pandas
- seaborn
- matplotlib
- scikit-learn
- dill
- catboost
- xgboost
- streamlit
