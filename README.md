# HHA-550-data-cleaning

## Diabetic Readmission Data Clean-up

This code is written in Python to clean up a diabetic readmission dataset. The code uses the pandas and numpy libraries to perform the necessary operations on the dataset. The dataset is stored in a CSV file, and the code reads the dataset and performs the following operations:

Drops the rows with missing values.
Replaces the "?" and "" values with NaN.
Drops the columns with missing values.
Converts the categorical variables to numerical variables using a data dictionary.
Counts the number of NaN values remaining in each column to ensure the dataset was cleaned properly.
Exports the data dictionary to a CSV file.
Exports the cleaned dataset to a CSV file.
The desired columns in the cleaned dataset are gender, age, max_glu_serum, A1Cresult, metformin, insulin, change, diabetesMed, and readmitted. The code defines a function create_data_dictionary that takes the dataset and desired columns as input, creates data dictionaries for the categorical variables, and returns the data dictionaries. The function also prints the data dictionaries for each column.

The cleaned dataset is stored in a CSV file named diabetic_data_cleaned.csv and the data dictionary is stored in a CSV file named data_dictionaries.csv.