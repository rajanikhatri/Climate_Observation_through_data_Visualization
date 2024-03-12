

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Temperature_file =pd.read_csv('/Users/rajanikhatri/Desktop/Project2/GlobalLandTemperaturesByState.csv')

# Converting the 'dt' column to datetime format
Temperature_file['dt'] = pd.to_datetime(Temperature_file['dt'], errors='coerce')

# Removing rows with null values in 'AverageTemperature' and 'AverageTemperatureUncertainty'
Temperature_file.dropna(subset=['AverageTemperature', 'AverageTemperatureUncertainty'], inplace=True)

# Finding and displaying duplicate rows in the entire DataFrame
duplicate_rows = Temperature_file.duplicated().sum()

# Printing the duplicate rows
print("Number of duplicates rows", duplicate_rows)

Temperature_file.drop_duplicates(inplace=True)

#process of removing the outliers
 #visualizing the data using boxplot and check if the columns contains outliers or not
def plot_boxplot(a,b):#two arguments dataframe and feature
 a.boxplot(column=[b])
 plt.grid(False)
 plt.show()
plot_boxplot(Temperature_file,"AverageTemperatureUncertainty")
plot_boxplot(Temperature_file,"AverageTemperature")
#removing outliers
def outliers(a,b):
  Q1 = a[b].quantile(0.25)#1st quantile
  Q3 = a[b].quantile(0.75)#3rd quantile
  IQR = Q3 - Q1 #inter quantile range
  lower_bound = Q1 - 1.5 * IQR
  upper_bound = Q3 + 1.5 * IQR
  my_list = a.index [(a[b]<lower_bound )|(a[b]>upper_bound) ] 
  return my_list
# creating an empty list to store the output indices from multiple columns
index_list = []
#using for loop to extract all the outliers
for column in ['AverageTemperature','AverageTemperatureUncertainty']:
  index_list.extend(outliers(Temperature_file,column))
#defining  a function called "remove" which returns a cleaned dataframe without outliers
def remove(a,my_list):#two input arguments name dataframe and index list
  list = sorted(set(my_list))#index list maynot be sorted so we using sorted function
  a = a.drop(my_list)#to remove the rows which contains outliers we using drop function to remove it.
  return a
#Cleaning the data by removing outliers from both columns
cleaned_temperature_data = remove(Temperature_file,index_list)
print(cleaned_temperature_data)

#making sure "dt" column is in datetime format
cleaned_temperature_data['dt'] = pd.to_datetime(cleaned_temperature_data['dt'], errors='coerce')

# Splitting the data into two parts: before 1899 and from 1900 to 2013
data_before_1899 = cleaned_temperature_data[cleaned_temperature_data['dt'] < '1899-01-01']
data_1900_to_2013 = cleaned_temperature_data[(cleaned_temperature_data['dt'] >= '1900-01-01') & (cleaned_temperature_data['dt'] <= '2013-12-31')]

# Print the first few rows of each segment
print("Data Before 1899:")
print(data_before_1899.head())

print("\nData from 1900 to 2013:")
print(data_1900_to_2013.head())

#piechart
# Filtering out rows where both 'AverageTemperature' and 'AverageTemperatureUncertainty' are non-negative
removing_negatives = cleaned_temperature_data[
    (cleaned_temperature_data['AverageTemperature'] >= 0) & 
    (cleaned_temperature_data['AverageTemperatureUncertainty'] >= 0)
].dropna(subset=['AverageTemperature', 'AverageTemperatureUncertainty'])

#grouping the dataset by country and getting the sum
country_grouping= removing_negatives.groupby('Country')[['AverageTemperature','AverageTemperatureUncertainty']].sum()


# Plotting two separate Pie charts for AverageTemperatureUncertainty and AverageTemperature
fig, axs = plt.subplots(1, 2, figsize=(14,10))

# First Pie chart for AverageTemperatureUncertainty
axs[0].pie(country_grouping['AverageTemperatureUncertainty'], labels=country_grouping.index, startangle=0, autopct='%2.1f%%')
axs[0].set_title("Average Temperature Uncertainty Share by Country")

# Second Pie chart for AverageTemperature
axs[1].pie(country_grouping['AverageTemperature'], labels=country_grouping.index, startangle=0, autopct='%2.1f%%')
axs[1].set_title("Average Temperature Share by Country")
plt.show()

#linegraph
# Function to filter data based on date range and create a line plot
def plot_temperature_data(cleaned_temperature_data):
    # Getting a random country from the dataset
    random_country_selection = np.random.choice(cleaned_temperature_data['Country'].unique())
    print(f'Selected Country: {random_country_selection}')  # Printing the selected country

    # Filter data for the selected country
    selected_country_data_before_1899 = data_before_1899[data_before_1899['Country'] == random_country_selection]
    selected_country_data_1900_to_2013 = data_1900_to_2013[data_1900_to_2013['Country'] == random_country_selection]

    # Plotting the lines
    plt.figure(figsize=(10, 6))
    plt.plot(selected_country_data_before_1899['dt'], selected_country_data_before_1899['AverageTemperature'], label='Before 1899')
    plt.plot(selected_country_data_1900_to_2013['dt'], selected_country_data_1900_to_2013['AverageTemperature'], label='After 1900')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (Celsius)')
    plt.title(f'Average Temperature Over Time - {random_country_selection}')
    plt.legend()
    plt.show()
plot_temperature_data(cleaned_temperature_data)

#scatter plot 
# Selecting a subset of countries (e.g., 5 countries) for the scatter plot
selected_countries = np.random.choice(cleaned_temperature_data['Country'].unique(), size=5, replace=False)

# Filtering data for selected countries
selected_countries_data = cleaned_temperature_data[cleaned_temperature_data['Country'].isin(selected_countries)]

plt.figure(figsize=(12, 8))
plt.scatter(selected_countries_data['Country'], selected_countries_data['AverageTemperature'], alpha=0.5)
plt.xlabel('Country')
plt.ylabel('Average Temperature (Celsius)')
plt.title('Scatter Plot of Average Temperature for Selected Countries')
plt.xticks(rotation=45, ha='right')  # Rotate country names for better visibility
plt.show()

#Bar Plot
# Grouping data by state and calculating the temperature difference
state_temperature_diff = data_1900_to_2013.groupby('State').apply(lambda group: group['AverageTemperature'].max() - group['AverageTemperature'].min())

# Sorting the states based on temperature difference and selecting the top 50
top_50_states = state_temperature_diff.sort_values(ascending=False).head(50)

# Bar plot for the top 50 states
plt.figure(figsize=(14, 8))
top_50_states.plot(kind='bar', color='skyblue')
plt.xlabel('State')
plt.ylabel('Temperature Difference (Celsius)')
plt.title('Temperature Difference (Max - Min) After 1900 for Top 50 States')
plt.xticks(rotation=45, ha='right')  # Rotate state names for better visibility
plt.show()


# Selecting two countries
country1 = np.random.choice(cleaned_temperature_data['Country'].unique())
country2 = np.random.choice(cleaned_temperature_data['Country'].unique())

# Filtering data for the selected countries
data_country1 = cleaned_temperature_data[cleaned_temperature_data['Country'] == country1]
data_country2 = cleaned_temperature_data[cleaned_temperature_data['Country'] == country2]

# Calculating the average temperatures for each country
avg_temp_country1 = data_country1['AverageTemperature'].mean()
avg_temp_country2 = data_country2['AverageTemperature'].mean()

# Calculating the TVD
tvd = abs(avg_temp_country1 - avg_temp_country2) / 2

print(f"Selected Countries: {country1} and {country2}")
print(f"Average Temperature for {country1}: {avg_temp_country1:.2f} °C")
print(f"Average Temperature for {country2}: {avg_temp_country2:.2f} °C")
print(f"Total Variation Distance (TVD): {tvd:.2f} °C")

#Question no 6 answer:
#why there is such largest temperature change in Novosibirsk state?
#Ans :The largest temperature change observed in Novosibirsk state could be influenced by
#  various factors. Geographical location, climate zones, land use changes, and 
# natural climate variability play roles in determining regional temperatures. 
# Additionally, global climate change and data anomalies should be considered. 
# A comprehensive analysis of historical climate data, local meteorological records, and consultation with 
# experts is necessary to understand the specific reasons for the observed temperature fluctuations in Novosibirsk state.