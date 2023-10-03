import pandas as pd  # Import the Pandas library and alias it as 'pd' for easier usage.
from matplotlib import pyplot as plt  # Import the 'pyplot' module from Matplotlib for plotting and alias it as 'plt'.
import seaborn as sns  # Import the Seaborn library for enhanced data visualization.
import os  # Import the 'os' module to interact with the operating system.
from sklearn.preprocessing import MinMaxScaler  # Import MinMaxScaler from scikit-learn for feature scaling.
from sklearn.model_selection import train_test_split  # Import train_test_split for data splitting.
from sklearn.linear_model import LogisticRegression  # Import the LogisticRegression model for classification.
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix  # Import metrics for model evaluation.

# Define file paths for training and test datasets.
file_path_training = "C:/Users/omosh/OneDrive/Documents/yESA/archive/churn-bigml-20.csv"
file_path_test = "C:/Users/omosh/OneDrive/Documents/yESA/archive/churn-bigml-20.csv"

# Read the training and test datasets into Pandas DataFrames.
df = pd.read_csv(file_path_training)
df_t = pd.read_csv(file_path_test)

# Create an output directory named 'figures' if it doesn't exist.
output_directory = 'figures/'
os.makedirs(output_directory, exist_ok=True)

# Divide the columns into categorical and quantitative types for easier data handling.
categorical_columns = df.select_dtypes(include=['object']).columns
quantitative_columns = df.select_dtypes(include=['int', 'float']).columns

# Create a list of numerical columns by selecting those of numeric data types.
numerical_columns = df.select_dtypes(include=['number']).columns.tolist()

# Create a list of categorical columns by selecting those that are not numeric.
categorical_columns = df.select_dtypes(exclude=['number']).columns.tolist()

# Print the lists of numerical and categorical columns.
print("Numerical Columns:", numerical_columns)
print("Categorical Columns:", categorical_columns)

# Create histograms to visualize the distribution of numerical columns.
for column in numerical_columns:
    plt.figure(figsize=(8, 6))  # Set the size of the plot.
    sns.histplot(data=df, x=column, bins=20, kde=True, color='red')  # Create a histogram using Seaborn.
    plt.xlabel(column)  # Set the x-axis label.
    plt.ylabel('Frequency')  # Set the y-axis label.
    plt.title(f'Distribution of {column}')  # Set the title of the plot.
    output_path = os.path.join(output_directory, f'{column}_countplot.png')  # Define the output file path.
    plt.savefig(output_path)  # Save the plot as an image.
    plt.show()  # Display the plot.
    plt.close()  # Close the current plot to prepare for the next one.
