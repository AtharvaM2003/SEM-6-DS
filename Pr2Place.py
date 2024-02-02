# Create an “Academic performance” dataset of students and perform the following operations using Python.
# 1. Scan all variables for missing values and inconsistencies. If there are missing values and/or inconsistencies, use any of the suitable techniques to deal with them.
# 2. Scan all numeric variables for outliers. If there are outliers, use any of the suitable techniques to deal with them.
# 3. Apply data transformations on at least one of the variables. The purpose of this transformation should be one of the following reasons: to change the scale for better understanding of the variable, to convert a non-linear relation into a linear one, or to decrease the skewness and convert the distribution into a normal distribution.
import pandas as pd
import numpy as np

# Create a sample dataset with at least 30 records
data = {
    'math_score': np.random.randint(60, 101, 30),
    'reading_score': np.random.randint(60, 101, 30),
    'writing_score': np.random.randint(60, 101, 30),
    'placement_score': np.random.randint(71, 101, 30),
    'club_join_date': pd.date_range('2022-01-01', periods=30, freq='D')
}

df = pd.DataFrame(data)

# Function to provide offer letter based on placement_score
def get_offer_letter(placement_score):
    if 71 <= placement_score <= 80:
        return 0
    elif 81 <= placement_score <= 90:
        return 1
    elif 91 <= placement_score <= 100:
        return 2
    else:
        return None

# Apply the function to create the 'offer_letter' column
df['offer_letter'] = df['placement_score'].apply(get_offer_letter)

# Display the resulting DataFrame
print("Original DataFrame:")
print(df)

# Randomly delete 10 values from any column
for _ in range(10):
    random_row_index = np.random.choice(df.index)
    random_column = np.random.choice(df.columns)
    df.loc[random_row_index, random_column] = np.nan

# Display the DataFrame after deleting 10 random values
print("\nDataFrame after deleting 10 random values:")
print(df)
print(df.isnull())