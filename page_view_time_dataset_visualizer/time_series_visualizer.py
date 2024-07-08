import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates= ['date'])
df.index = df['date']
df = df.drop(columns = ['date'])

# Clean data
filter_1 = df['value'] >= df['value'].quantile(0.025)
filter_2 = df['value'] <= df['value'].quantile(0.975)
filtered = filter_1 & filter_2
df = df[filtered]


# print(df_bar.columns)

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (10,5))
    ax.plot(df.index, df['value'], 'r')
    ax.set_xlabel ('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_b = df.copy()
    df_b['year'] = df_b.index.year
    df_b['month'] = df_b.index.month
    df_bar = df_b.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot.bar(legend = True, xlabel = 'Years',
                          ylabel = 'Average Page Views').figure
    plt.legend([
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"])
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows = 1, ncols = 2, figsize = (15,5))
    ax[0] = sns.boxplot(x = df_box['year'], y = df_box['value'], ax = ax[0],
                        palette = sns.color_palette("pastel"))
    ax[1] = sns.boxplot(x = df_box['month'], y = df_box['value'], ax = ax[1],
                        order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov', 'Dec'],
                        palette = sns.color_palette("pastel"))
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')

    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    plt.tight_layout()
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
