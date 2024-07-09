import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot(): 

    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    linr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_1 = np.arange(int(df['Year'].min()), 2051)
    y_1 = linr.slope * x_1 + linr.intercept
    plt.plot(x_1,y_1, label = 'Line of best fit')

    # Create second line of best fit
    filter_1 = (df['Year'] >= 2000) & (df['Year'] <= (df['Year'].max()))
    df_filtered = df[filter_1]
    linr_2 = linregress(df_filtered['Year'], df_filtered['CSIRO Adjusted Sea Level'])
    x_2 = np.arange(int(df_filtered['Year'].min()), 2051)
    y_2 = linr_2.slope * x_2 + linr_2.intercept
    plt.plot(x_2,y_2, label = 'Line of best fit between years 2000 a 2050')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.grid()    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

