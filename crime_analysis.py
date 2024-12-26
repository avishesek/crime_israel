import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV files for years 2019-2024
crime2024 = pd.read_csv(r'C:\avishai\crimes_israel_2019_2024\crime_israel\data\crimes2024.csv')
crime2023 = pd.read_csv(r'C:\avishai\crimes_israel_2019_2024\crime_israel\data\crimes2023.csv')
crime2022 = pd.read_csv(r'C:\avishai\crimes_israel_2019_2024\crime_israel\data\crimes2022.csv')
crime2021 = pd.read_csv(r'C:\avishai\crimes_israel_2019_2024\crime_israel\data\crimes2021.csv')
crime2020 = pd.read_csv(r'C:\avishai\crimes_israel_2019_2024\crime_israel\data\crimes2020.csv')
crime2019 = pd.read_csv(r'C:\avishai\crimes_israel_2019_2024\crime_israel\data\crimes2019.csv')

# Clean the data: Remove entries with invalid `StatisticGroupKod` values
datasets = [crime2024, crime2023, crime2022, crime2021, crime2020, crime2019]
datasets = [df[df['StatisticGroupKod'] != -1] for df in datasets]

# Combine data from all years into one DataFrame
crime = pd.concat(datasets, axis=0)


# Remove duplicate entries based on 'FictiveIDNumber'
crime_no_dup = crime.drop_duplicates(subset='FictiveIDNumber',keep='last')

# Define government mapping based on year and quarter
government_mapping = {
    (2019, 'Q1'): '34', (2019, 'Q2'): '34', (2019, 'Q3'): '34-transition', (2019, 'Q4'): '34-transition',
    (2020, 'Q1'): '34-transition', (2020, 'Q2'): '34-transition', (2020, 'Q3'): '35', (2020, 'Q4'): '35',
    (2021, 'Q1'): '35', (2021, 'Q2'): '35', (2021, 'Q3'): '36', (2021, 'Q4'): '36',
    (2022, 'Q1'): '36', (2022, 'Q2'): '36', (2022, 'Q3'): '37', (2022, 'Q4'): '37',
    (2023, 'Q1'): '37', (2023, 'Q2'): '37', (2023, 'Q3'): '37', (2023, 'Q4'): '37',
    (2024, 'Q1'): '37', (2024, 'Q2'): '37', (2024, 'Q3'): '37', (2024, 'Q4'): '37',
}

# Add a 'Government' column based on mapping
crime_gov = crime.copy()
crime_gov['Government'] = crime_gov.apply(lambda row: government_mapping.get((row['Year'], row['Quarter']), 'Unknown'), axis=1)

# Add a 'Government' column based on mapping
crime_gov_no_du = crime_no_dup.copy()
crime_gov_no_du['Government'] = crime_gov_no_du.apply(lambda row: government_mapping.get((row['Year'], row['Quarter']), 'Unknown'), axis=1)


# Filter data for crimes against humans

ag_pe_crime = crime[crime['StatisticGroup'] == 'עבירות נגד אדם'] # for yearly no gov
ag_pe_crime_no_dup = ag_pe_crime.drop_duplicates(subset='FictiveIDNumber',keep='last') # drop duplicates

# Categorize specific crime types
pepole_life_crime = ag_pe_crime_no_dup[ag_pe_crime_no_dup['StatisticTypeKod'] != 302]
terror = ag_pe_crime[ag_pe_crime['StatisticTypeKod'] == 302]
morder = ag_pe_crime[ag_pe_crime['StatisticTypeKod'] == 301]
deaths = ag_pe_crime[ag_pe_crime['StatisticTypeKod'].isin((301,306,307, 305)) ]


# quarterly data with gov
ag_pe_crime_gov = crime_gov[crime_gov['StatisticGroup'] == 'עבירות נגד אדם'] # human life
ag_pe_crime_gov_no_dup = ag_pe_crime_gov.drop_duplicates(subset='FictiveIDNumber',keep='last') # drop duplicates

# Categorize specific crime types
pepole_life_crime_gov = ag_pe_crime_gov_no_dup[ag_pe_crime_gov_no_dup['StatisticTypeKod'] != 302]
terror_gov = ag_pe_crime_gov[ag_pe_crime_gov['StatisticTypeKod'] == 302]
morder_gov = ag_pe_crime_gov[ag_pe_crime_gov['StatisticTypeKod'] == 301]
deaths_gov = ag_pe_crime_gov[ag_pe_crime_gov['StatisticTypeKod'].isin((301,306,307, 305)) ]

# check if they are duplicates
# function to print if duplicated
def duplicate(df,name):
    df_dup = df.duplicated(subset=['StatisticTypeKod', 'FictiveIDNumber'], keep=False)
    if sum(df_dup) == 0:
        print('no duplicates in '+name+' data')

# print if duplicate in the data
duplicate(deaths_gov, 'deaths_gov')
duplicate(morder_gov, 'morder_gov')
duplicate(terror_gov, 'terror_gov')
duplicate(deaths, 'deaths')
duplicate(morder, 'morder')
duplicate(terror, 'terror')

# the plots

# yearly plots

def plotcrimeyearly(df, st):
    # create table for plot
    # Count crimes per year
    crimes_per_y = df['Year'].value_counts().sort_index()

    # Plot the data
    plt.figure(figsize=(8, 5))
    barplot = sns.barplot(x=crimes_per_y.index, y=crimes_per_y.values, color='blue')

    # Add labels on the bars
    for bar, value in zip(barplot.patches, crimes_per_y.values):
        barplot.text(
            bar.get_x() + bar.get_width() / 2,  # X-coordinate
            bar.get_height(),  # Y-coordinate (height of the bar)
            f'{value}',  # Label text
            ha='center', va='bottom',  # Align horizontally and vertically
            fontsize=10  # Font size
        )

    # Add labels and title
    plt.title('Number of open cases of ' +st+ ' per Year (2019-2024)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Crimes', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    # Save the graph to the project folder
    # st_name = st.replace(" ", "_") # remove the hash to save on your PC
    # plt.savefig('yearly_graph_'+st_name+'.png') # remove the hash to save on your PC
    # Show the plot
    plt.show()


plotcrimeyearly(crime_no_dup,'Crimes' )
plotcrimeyearly(pepole_life_crime ,'Crime Against Human Life')
plotcrimeyearly(morder ,'Morders')
plotcrimeyearly(terror ,'Morders from Acts Of Terrorism')
plotcrimeyearly(deaths ,'Death')


# quarter plots
def plotcrime(df, st):
    # Group by Year, Quarter, and Government to count crimes
    df = df.groupby(['Year', 'Quarter', 'Government']).size().reset_index(
        name='CrimeCount')

    # Combine Year and Quarter for plotting purposes
    df['Year_Quarter'] = df['Year'].astype(str) + ' ' + df['Quarter']

    # Plot the data
    plt.figure(figsize=(12, 6))
    barplot = sns.barplot(
        data=df,
        x='Year_Quarter',
        y='CrimeCount',
        hue='Government',
        palette='viridis'
        )

    # Add labels on the bars
    for bar, value in zip(barplot.patches, [f'{int(ba.get_height())}' for ba in barplot.patches]):
        barplot.text(
            bar.get_x() + bar.get_width() / 2,  # X-coordinate
            bar.get_height(),  # Y-coordinate (height of the bar)
            f'{value}',  # Label text
            ha='center', va='bottom',  # Align horizontally and vertically
            fontsize=10  # Font size
        )

    # Add labels and title
    plt.title('Number of open cases of ' +st+ ' by Year, Quarter, and Government', fontsize=16)
    plt.xlabel('Year and Quarter', fontsize=12)
    plt.ylabel('Number of Crimes', fontsize=12)
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(title='Government', fontsize=10, loc='upper left')
    plt.tight_layout()
    # Save the graph to the project folder
    # st_name = st.replace(" ", "_") # remove the hash to save on your PC
    # plt.savefig('quarterly_graph_' + st_name + '.png') # remove the hash to save on your PC
    # Show the plot
    plt.show()

# plot the open crime cases by each parametter
plotcrime(crime_gov_no_du,'Crimes')
plotcrime(pepole_life_crime_gov ,'Crime Against Human Life')
plotcrime(morder_gov ,'Morders')
plotcrime(terror_gov ,'Morders from Acts Of Terrorism')
plotcrime(deaths_gov ,'Deaths')

