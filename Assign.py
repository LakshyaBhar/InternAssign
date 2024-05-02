import pandas as pd
import matplotlib.pyplot as plt

# Function to read test and label files
def read_data(test_file, label_file):
    test_data = pd.read_csv(test_file)
    label_data = pd.read_csv(label_file)
    return test_data, label_data

# Function to draw time series plots with anomaly regions
def plot_time_series(test_data, label_data):
    plt.figure(figsize=(12, 6))
    plt.plot(test_data['timestamp'], test_data['value'], color='blue', label='Time Series Data')
    anomalies = label_data['timestamp']
    for anomaly in anomalies:
        plt.axvline(x=anomaly, color='red', linestyle='--', linewidth=2, label='Anomaly')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Time Series Plot with Anomaly Regions')
    plt.legend()
    plt.show()

# Function to perform EDA and find out root cause
def perform_eda(test_data, label_data):
    # Here you can perform exploratory data analysis to identify patterns or anomalies in the data.
    # You can analyze statistical measures, visualize data distributions, etc.
    # Identify any patterns or correlations that may suggest root causes for anomalies.
    # For example, you can use descriptive statistics, correlation analysis, or visualization techniques.

    # Example EDA:
    # Check for missing values
    missing_values = test_data.isnull().sum()
    print("Missing Values:\n", missing_values)

    # Check data types
    data_types = test_data.dtypes
    print("Data Types:\n", data_types)

    # Summary statistics
    summary_stats = test_data.describe()
    print("Summary Statistics:\n", summary_stats)

# Function to find out variables which are the root cause for the anomaly
def find_root_cause(test_data, label_data):
    # Here you can analyze the data to identify variables that may be the root cause of anomalies.
    # This may involve analyzing correlations, feature importance, or domain knowledge.

    # Example: Check correlation between variables and anomaly labels
    merged_data = pd.merge(test_data, label_data, on='timestamp', how='left')
    correlation_matrix = merged_data.corr()
    print("Correlation with Anomaly Label:\n", correlation_matrix['value'])

    # Identify variables with significant correlation or importance
    # For example, variables with high correlation coefficients or feature importance scores.

# Main code
if __name__ == "__main__":
    # Read test and label files
    test_data, label_data = read_data('test.csv', 'test_labels.csv')

    # Draw time series plots with anomaly regions
    plot_time_series(test_data, label_data)

    # Perform EDA and find out root cause
    perform_eda(test_data, label_data)

    # Find out variables which are the root cause for the anomaly
    find_root_cause(test_data, label_data)
