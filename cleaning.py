import pandas as pd
import numpy as np

data = pd.read_csv('Data/diabetic_data.csv')

# Drop the rows with missing values
data = data.dropna()
data.replace('?', pd.np.nan, inplace=True)
data.replace('', pd.np.nan, inplace=True)
# Drop the columns with missing values
data = data.dropna(axis=1)

# Create data dictionary for the desired columns
columns = ['gender', 'age', 'max_glu_serum', 'A1Cresult', 'metformin', 'insulin', 'change', 'diabetesMed', 'readmitted']
# Defining a function to create data dictionaries for the desired columns
def create_data_dictionary(data, columns):
    data_dictionaries = {}
    for col in columns:
        unique_values = data[col].unique()
        data_dict = dict(zip(unique_values, range(len(unique_values))))
        data_dictionaries[col] = data_dict
        print(f"Data Dictionary for df.{col}:")
        print(data_dict)
        print()
    return data_dictionaries
data_dictionaries = create_data_dictionary(data, columns)

# Converting the categorical variables to numerical variables
data.replace(data_dictionaries, inplace=True)

# Counting the number of NaN values remaining in each column to ensure dataset was cleaned properly
print(data.isna().sum())

# Exporting the data dictionary to a csv file
data_dictionaries_df = pd.DataFrame(data_dictionaries)

data_dictionaries_df.to_csv('Data/data_dictionaries.csv', index=False)

# Exporting the cleaned dataset to a csv file
data.to_csv('Data/diabetic_data_cleaned.csv', index=False)

### I think this is it ### 