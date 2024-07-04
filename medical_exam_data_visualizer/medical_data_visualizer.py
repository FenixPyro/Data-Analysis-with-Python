""" Module that contains functions for the visualization"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_exam_data_visualizer\medical_examination.csv')

# Calculate BMI and determine overweight status
BMI = (df['weight']) / (df['height'] / 100)**2
overweight_check = BMI > 25
df['overweight'] = overweight_check.astype(int)

# Normalize cholesterol and glucose values
cholesterol_check = df['cholesterol'] != 1
gluc_check = df['gluc'] != 1
df['cholesterol'] = cholesterol_check.astype(int)
df['gluc'] = gluc_check.astype(int)

def draw_cat_plot():
    """Generate a categorical plot (bar plot) grouped by the cardio's value.

    Returns:
        matplotlib.figure.Figure: The generated figure object.
    """
    df_cat = pd.melt(df, id_vars = ['cardio'],
                      value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
                    )
    df_cat['total']= 1
    df_cat = df_cat.groupby(['cardio','variable','value'], as_index = False).count()
    fig = sns.catplot(x='variable', y = 'total', hue='value', col='cardio', data=df_cat, kind='bar')
    fig = fig.figure
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    """Generate a heatmap showing the correlation of variables in the filtered DataFrame.

    Returns:
        matplotlib.figure.Figure: The generated figure object.
    """
    filter_1 = df['height'] >= df['height'].quantile(0.025)
    filter_2 = df['height'] <= df['height'].quantile(0.975)
    filter_3 = df['weight'] >= df['weight'].quantile(0.025)
    filter_4 = df['weight'] <= df['weight'].quantile(0.975)
    df_filter = filter_1 & filter_2 & filter_3 & filter_4
    df_heat = df[df_filter]

    corr = df_heat.corr()
    mask = np.triu(corr)
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.heatmap(corr, linewidths =1, square = True, ax=ax, mask = mask, fmt='.1f', annot=True)
    fig = fig.figure
    fig.savefig('heatmap.png')
    return fig
