# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from the provided data
data = {
    'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014],
    'Country': ['Uruguay', 'Italy', 'France', 'Brazil', 'Switzerland', 'Sweden', 'Chile', 'England', 'Mexico', 'Germany', 'Argentina', 'Spain', 'Mexico', 'Italy', 'USA', 'France', 'Korea/Japan', 'Germany', 'South Africa', 'Brazil'],
    'Winner': ['Uruguay', 'Italy', 'Italy', 'Uruguay', 'Germany FR', 'Brazil', 'Brazil', 'England', 'Brazil', 'Germany FR', 'Argentina', 'Italy', 'Argentina', 'Germany FR', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany'],
    'Runners-Up': ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Hungary', 'Sweden', 'Czechoslovakia', 'Germany FR', 'Italy', 'Netherlands', 'Netherlands', 'Germany FR', 'Germany FR', 'Argentina', 'Italy', 'Brazil', 'Germany', 'France', 'Netherlands', 'Argentina'],
    'Third': ['USA', 'Germany', 'Brazil', 'Sweden', 'Austria', 'France', 'Chile', 'Portugal', 'Germany FR', 'Poland', 'Brazil', 'Poland', 'France', 'Italy', 'Sweden', 'Croatia', 'Turkey', 'Germany', 'Germany', 'Netherlands'],
    'Fourth': ['Yugoslavia', 'Austria', 'Sweden', 'Spain', 'Uruguay', 'Germany FR', 'Yugoslavia', 'Soviet Union', 'Uruguay', 'Brazil', 'Italy', 'France', 'Belgium', 'England', 'Bulgaria', 'Netherlands', 'Korea Republic', 'Portugal', 'Uruguay', 'Brazil'],
    'GoalsScored': [70, 70, 84, 88, 140, 126, 89, 89, 95, 97, 102, 146, 132, 115, 141, 171, 161, 147, 145, 171],
    'QualifiedTeams': [13, 16, 15, 13, 16, 16, 16, 16, 16, 16, 16, 24, 24, 24, 24, 32, 32, 32, 32, 32],
    'MatchesPlayed': [18, 17, 18, 22, 26, 35, 32, 32, 32, 38, 38, 52, 52, 52, 52, 64, 64, 64, 64, 64],
    'Attendance': [590549, 363, 375700, 1045246, 768607, 819810, 893172, 1563135, 1603975, 1865753, 1545791, 2109723, 2394031, 2516215, 3587538, 2785100, 2705197, 3359439, 3178856, 3386810]
}

df = pd.DataFrame(data)

# Create visualizations
plt.figure(figsize=(15, 10))

# Bar plot for the number of World Cup Wins by Country
plt.subplot(2, 2, 1)
sns.countplot(x='Winner', data=df, palette='viridis')
plt.title('Number of World Cup Wins by Country')
plt.xlabel('Country')
plt.ylabel('Number of Wins')
plt.xticks(rotation=45)

# Donut plot for the distribution of World Cup Wins by Country
plt.subplot(2, 2, 2)
winner_counts = df['Winner'].value_counts()
labels = winner_counts.index
sizes = winner_counts.values
colors = sns.color_palette('viridis', len(labels))

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Distribution of World Cup Wins by Country')

# Line plot for Goals Scored over the years
plt.subplot(2, 2, 3)
sns.lineplot(x='Year', y='GoalsScored', data=df, marker='o', color='blue')
plt.title('Goals Scored in FIFA World Cup Over the Years')
plt.xlabel('Year')
plt.ylabel('Goals Scored')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from the provided data
data = {
    'Year': [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014],
    'Country': ['Uruguay', 'Italy', 'France', 'Brazil', 'Switzerland', 'Sweden', 'Chile', 'England', 'Mexico', 'Germany', 'Argentina', 'Spain', 'Mexico', 'Italy', 'USA', 'France', 'Korea/Japan', 'Germany', 'South Africa', 'Brazil'],
    'Winner': ['Uruguay', 'Italy', 'Italy', 'Uruguay', 'Germany FR', 'Brazil', 'Brazil', 'England', 'Brazil', 'Germany FR', 'Argentina', 'Italy', 'Argentina', 'Germany FR', 'Brazil', 'France', 'Brazil', 'Italy', 'Spain', 'Germany'],
    'Runners-Up': ['Argentina', 'Czechoslovakia', 'Hungary', 'Brazil', 'Hungary', 'Sweden', 'Czechoslovakia', 'Germany FR', 'Italy', 'Netherlands', 'Netherlands', 'Germany FR', 'Germany FR', 'Argentina', 'Italy', 'Brazil', 'Germany', 'France', 'Netherlands', 'Argentina'],
    'Third': ['USA', 'Germany', 'Brazil', 'Sweden', 'Austria', 'France', 'Chile', 'Portugal', 'Germany FR', 'Poland', 'Brazil', 'Poland', 'France', 'Italy', 'Sweden', 'Croatia', 'Turkey', 'Germany', 'Germany', 'Netherlands'],
    'Fourth': ['Yugoslavia', 'Austria', 'Sweden', 'Spain', 'Uruguay', 'Germany FR', 'Yugoslavia', 'Soviet Union', 'Uruguay', 'Brazil', 'Italy', 'France', 'Belgium', 'England', 'Bulgaria', 'Netherlands', 'Korea Republic', 'Portugal', 'Uruguay', 'Brazil'],
    'GoalsScored': [70, 70, 84, 88, 140, 126, 89, 89, 95, 97, 102, 146, 132, 115, 141, 171, 161, 147, 145, 171],
    'QualifiedTeams': [13, 16, 15, 13, 16, 16, 16, 16, 16, 16, 16, 24, 24, 24, 24, 32, 32, 32, 32, 32],
    'MatchesPlayed': [18, 17, 18, 22, 26, 35, 32, 32, 32, 38, 38, 52, 52, 52, 52, 64, 64, 64, 64, 64],
    'Attendance': [590549, 363, 375700, 1045246, 768607, 819810, 893172, 1563135, 1603975, 1865753, 1545791, 2109723, 2394031, 2516215, 3587538, 2785100, 2705197, 3359439, 3178856, 3386810]
}

df = pd.DataFrame(data)

# Count the number of times each country finished in the top four
top_four_counts = pd.concat([df['Winner'], df['Runners-Up'], df['Third'], df['Fourth']]).value_counts()

# Create a horizontal bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=top_four_counts.values, y=top_four_counts.index, palette='muted')
plt.title('Number of Times Each Country Finished in the Top Four')
plt.xlabel('Number of Times')
plt.ylabel('Country')

plt.show()
