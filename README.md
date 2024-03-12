# Climate Change Analysis Project

## Overview

This project conducts a detailed analysis of global land temperatures by state, aiming to observe and understand the changes in temperature and their potential causes. Leveraging data preprocessing and exploratory data analysis (EDA) techniques, this study provides insights into climate change trends and their implications across various regions.

## Dataset

The primary dataset used is `GlobalLandTemperaturesByState.csv`, which includes records of average land temperatures across different states and countries. Key columns in the dataset include:

- `dt`: The date when the temperature was recorded.
- `AverageTemperature`: The average land temperature in Celsius.
- `AverageTemperatureUncertainty`: The 95% confidence interval around the average temperature.
- `State`: The state name.
- `Country`: The country name.

## Methodology

### Data Preprocessing

The preprocessing steps involved:

1. **Date Conversion**: The `dt` column was converted into a unified datetime format to standardize date entries.
2. **Null Value Removal**: Rows with null values in `AverageTemperature` and `AverageTemperatureUncertainty` were removed to ensure data integrity.
3. **Duplicate Removal**: Duplicate rows across the dataset were identified and removed to maintain data uniqueness.
4. **Outlier Handling**: Outliers in `AverageTemperature` and `AverageTemperatureUncertainty` were identified using boxplots and removed to prevent skewed analysis.

### Data Segmentation

The dataset was split into two segments:
- Data before 1899.
- Data from 1900 to 2013.

This segmentation facilitates comparative analysis of temperature trends across different time periods.

### Exploratory Data Analysis (EDA)

1. **Pie Charts**: The dataset was grouped by country, and the sum of records for each country was used to display the share of average temperatures and temperature uncertainty across countries using pie charts.

2. **Line Graphs**: A country was randomly selected to compare the average temperatures before 1899 and after 1900 using line graphs. This involved filtering the data based on the selected country and the specified time periods, then plotting the average temperatures over time.

3. **Scatter Plot**: A scatter plot was generated to visualize the average temperatures of a subset of countries, showcasing the variability in climate across different regions.

4. **Bar Plot**: The temperature changes (difference between maximum and minimum temperatures) after 1900 for all states were plotted using a bar plot. The top 50 states with the largest temperature differences were highlighted to identify regions with significant climate variability.

5. **TVD Calculation**: The Total Variation Distance (TVD) between the average temperatures of two randomly selected countries was calculated to measure the disparity in climate changes between them.

6. **Analysis of Temperature Change**: An explanation was provided for the largest temperature change observed in a specific state, considering various factors like geographical location, climate zones, and global climate change impacts.

## Conclusion

This project utilized data cleaning, transformation, and various EDA techniques to analyze climate change trends. Through pie charts, line graphs, scatter plots, and bar plots, it offered insights into how temperatures have changed over time across different states and countries, contributing to a better understanding of global climate change patterns.

## Author

- Rajani Khatri
