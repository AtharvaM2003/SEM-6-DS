# 1: Import required libraries 
import pandas as pd 
# 2: Load the dataset into pandas dataframe 
file_path = 'iris.csv' 
df = pd.read_csv(file_path) 
# 3: Data Preprocessing
# Check for missing values 
missing_values = df.isnull().sum() 
# Describe the dataset to get initial statistics 
data_description = df.describe() 
# Variable descriptions and types 
variable_descriptions = df.dtypes 
# Check dimensions of the dataframe 
data_dimensions = df.shape 
# Print the results 
print("Missing Values:") 
print(missing_values) 
print("\nInitial Statistics:") 
print(data_description) 
print("\nVariable Descriptions and Types:") 
print(variable_descriptions) 
print("\nData Dimensions:") 
print(data_dimensions)