#A machine learning project, dealing with a large amount of data and normalizing the data

import pandas as pd
from pandas import DataFrame, Series
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("bitter_original.csv")

# change all bitter and non-bitter to binary values
df['ACTIVITY'].replace(['Bitter','Non-Bitter'] , [int(1),int(0)] ,inplace=True)


#Mixtape and text deletion
df = df.select_dtypes(exclude=['object'])
df.shape


#Modes containing more than 50% of the fields null/fixed value
ColumnsNames = df.drop('ACTIVITY' , axis = 1).columns.values
Non_Col_Values = []
for col in ColumnsNames:
  count_values = df[col].nunique(dropna = True)
  values_count = df[col].value_counts(dropna = True)
  if (values_count / len(df.index)).max() > 0.5:
    df.drop(col , inplace = True , axis = 1)

df=df.loc[:, (df.isna().sum() / len(df.index)) < 0.5]

df.shape




# Calculate means and standard deviations for each variable
means = df.mean()
stds = df.std()

# Calculate upper and lower bounds for identifying outliers for each variable
upper_bounds = means + 2 * stds
lower_bounds = means - 2 * stds

# Identify the outliers for each variable and count them for each row
outliers = (df > upper_bounds) | (df < lower_bounds)
outliers_count = outliers.sum(axis=1)

# Drop rows with more than 50% outliers
outliers_mask = outliers_count / len(df.columns) < 0.5
df = df.loc[outliers_mask, :]

# Check the shape of the DataFrame
df.shape



# calculate the correlation matrix
corr_matrix = df.corr()

# find the correlated variables
corr_variables = set()
for i in range(len(corr_matrix.columns)):
    for j in range(i):
        if abs(corr_matrix.iloc[i, j]) >= 0.8:
            corr_variables.add(corr_matrix.columns[i])

# remove one of the correlated variables
df = df.drop(corr_variables, axis=1)
df.shape
df.corr()


df.drop_duplicates(inplace = True)
df.shape



# Define a function to calculate the Z-score for a given value
def z_score(val, mean, std):
    return (val - mean) / std

# Find the mean and standard deviation for numeric columns 1 onwards
numeric_cols = df.select_dtypes(include='number').columns[0:]
means = df[numeric_cols].mean()
stds = df[numeric_cols].std()

# Calculate the Z-score for each value in numeric columns 1 onwards
normelize_df = df.loc[:]
for col in numeric_cols:
    normelize_df[col] = z_score(df[col], means[col], stds[col])


df.shape



box = normelize_df.boxplot(vert=False)

#if you wanna see the boxplot witount outliers , use the code above :
box1 = normelize_df.boxplot(showfliers = False ,vert=False)


df.hist(figsize=(20, 20))


# Define a dictionary to store the descriptive statistics
stats_dict = {}

# Iterate over each column in the dataframe
for col in df.columns:
    # Calculate the descriptive statistics based on the measurement scale
    if df[col].dtype == 'object':
        # For categorical variables, calculate the counts and the mode
        counts = df[col].value_counts()
        mode = df[col].mode().iloc[0]
        stats_dict[col] = {'Counts': counts, 'Mode': mode}
    elif df[col].dtype == 'int64' or df[col].dtype == 'float64':
        # For numerical variables, calculate the range, mean, and standard deviation
        r = df[col].min() , df[col].max()
        m = df[col].mean()
        sd = df[col].std()
        stats_dict[col] = {'Range': r, 'Mean': m, 'SD': sd}

# Convert the dictionary to a pandas dataframe
stats_df = pd.DataFrame(stats_dict)

# Transpose the dataframe to display the variables as rows instead of columns
stats_df = stats_df.T

# Print the resulting table
stats_df



normelize_df.to_excel("normelize_df.xlsx")
df.to_excel("df.xlsx")