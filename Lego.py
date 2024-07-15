import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sets.csv")

df.info

# Find the year the first LEGO sets were released and their names
earliest_year = df['year'].min()
names_of_earliest = df['name'][df['year']==1949]

# What are the top 5 LEGO sets with the most number of parts
num_parts = df.sort_values(by='num_parts', ascending=False).head()

year_index = df[['year', 'set_num']].groupby('year').count()

# Creating the graph canvas
plt.figure(figsize=(16,10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('year', fontsize =14)
plt.ylabel('Number of sets', fontsize =14)
plt.ylim(0,1000)
plt.title('sets by year', fontsize = 25)

# Plotting the line graph for number of sets
# plt.plot(year_index.index, year_index.set_num)
plt.plot(year_index.index[:-2], year_index.set_num[:-2])

########################### .agg FUNCTION #############################
themes_by_year = df.groupby('year').agg({'theme_id': pd.Series.nunique})

# Renaming columns
themes_by_year.rename(columns = {'theme_id': 'nr_themes'}, inplace=True)

themes_by_year.head()

themes_by_year.tail()

themes_df = pd.read_csv('themes.csv')

# Plot the number of themes released by year on a line chart. Only include the full years
plt.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2])

# Two separate axes on the same chart
# get the current axes
ax1 = plt.gca()
ax2 = ax1.twinx() # The twinx() method allows ax1 and ax2 to share the same x-axis

ax1.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='red')
ax2.plot(year_index.index[:-2], year_index.set_num[:-2])

parts_per_set = df.groupby('year').agg({'num_parts': pd.Series.mean})
parts_per_set.rename(columns = {'num_parts': 'average_num_parts'}, inplace=True)

############################## SCATTER ################################
plt.scatter(parts_per_set.index, parts_per_set.average_num_parts)

############################## MERGING DATAFRAMES ################################
set_theme_count = df["theme_id"].value_counts()

set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                                'set_count':set_theme_count.values})

merged_df = pd.merge(set_theme_count, themes_df, on ='id')
