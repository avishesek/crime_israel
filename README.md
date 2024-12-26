# Analysis of Crime Cases in Israel (2019-2024)

## Overview
This project aims to analyze crime cases in Israel from 2019 to 2024 based on open case records published by the Israel Police. The analysis explores:

1. Crime trends in recent years, especially in 2023 and 2024.
2. The correlation between different governments and crime statistics.
3. Changes in crimes involving harm to human life and murder.

## Data Sources
The data used in this project consists of public records from the Israel Police, specifically focusing on the number of cases opened each year.

**Important Notes about the Data:**
- It only includes cases involving Israeli citizens.
- It does not cover the number of complaints, victims, or convictions, only opened cases.
- Cases with duplicate or erroneous entries were filtered out for accuracy.
- 2024 data includes only up to the third quarter (up to October).

## Key Features
The analysis is divided into two main parts:

1. **Yearly Crime Data Analysis:**
   - Aggregates crime data for each year from 2019 to 2024.

2. **Quarterly Crime Data Analysis:**
   - Breaks down the crime data by year, quarter, and government in power during each period.
   - Focuses on correlations between governments and crime trends.

## Metrics and Visualizations
The project analyzes and visualizes the following:

1. **Overall Crime Cases:**
   - Number of all opened crime cases by year and quarter.

2. **Crimes Against Human Life:**
   - Crimes involving harm to human life, excluding acts of terrorism.

3. **Murders:**
   - Cases involving murder, analyzed separately.

4. **Deaths from Acts of Terrorism:**
   - Separate analysis for crimes categorized as terrorism.

5. **Deaths (Including Murder, Manslaughter, etc.):**
   - A broader category covering all deaths resulting from crimes.

## Data Preparation
1. **Data Cleaning**: Removed duplicate records and erroneous entries.
2. **Mapping Governments**: Mapped each quarter to the corresponding government in power.


## Visualizations
The visualizations and graphs appear in an additional readme file that appears under the name Visualizations.md.

The analysis includes the following visualizations:
1. Total crime cases (yearly and quarterly).
2. Crimes against human life (yearly and quarterly).
3. Murder cases (yearly and quarterly).
4. Death cases (including murder, manslaughter, etc.),(yearly and quarterly).
5. Murders due to terrorism (yearly and quarterly)


1. **Yearly Trends:** - Bar charts representing the number of crimes by year.

2. **Quarterly Trends by Government:** - Stacked bar charts showing the number of crimes by quarter, with government identification.

## Conclusions and Insights
The analysis provides nuanced insights into crime trends, including:
- A general decline in overall crime cases in 2023 and 2024 compared to previous years.
- A notable increase in crimes against human life in the same period.
- Quarterly data highlights changes in crime trends corresponding to different government tenures.

## Future Work
To enhance this project, the following steps are recommended:
1. **Expand Data Sources:**
   - Incorporate additional datasets, such as complaints, convictions, or demographic information of offenders.
2. **Analyze Crime by Sector:**
   - Investigate crime trends across different communities or sectors in Israel.
3. **Temporal Factors:**
   - Explore correlations between specific events (e.g., war, policy changes) and crime trends.

## How to Use This Repository
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Update the file paths in the script to match your local environment.
4. Run the analysis script and review the outputs and visualizations.


## Repository Structure
```
crime_israel/
|
|-- data/                   # Contains raw data files. (not in the folder due to space limitation,link to the data is under the Structure
|-- Visualizations.md/      # Generated plots.
|-- README.md               # Project overview (this file) and summaries.
|-- graghs/                 # The plots in pgn files.
```
[crime_israel](https://data.gov.il/dataset/crime_records_data)

## Acknowledgments
Special thanks to the Israel Police for publishing open data and enabling public analysis. Any conclusions drawn from this analysis are solely those of the author.
