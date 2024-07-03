import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_exam_data_visualizer/medical_examination.csv')

# 2
BMI = (df['weight']) / (df['height'] / 100)**2
overweight_check = BMI > 25
df['overweight'] = overweight_check.astype(int)

# 3
cholesterol_check = df['cholesterol'] != 1
gluc_check = df['gluc'] != 1
df['cholesterol'] = cholesterol_check.astype(int)
df['gluc'] = gluc_check.astype(int)

def draw_cat_plot():
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'],
                 var_name='variable', value_name='value')
    fig = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count')
    fig.savefig('catplot.png')
    return fig

# filter_1 = df['height'] >= df['height'].quantile(0.025)
# filter_2 = df['height'] <= df['height'].quantile(0.975)
# filter_3 = df['weight'] >= df['weight'].quantile(0.025)
# filter_3 = df['weight'] <= df['weight'].quantile(0.975)
# filter = filter_1 & filter_2 & filter_3 & filter_4
# df_cleaned_1 = df[filter]

# 10
def draw_heat_map():
    # 11
    filter_1 = df['height'] >= df['height'].quantile(0.025)
    filter_2 = df['height'] <= df['height'].quantile(0.975)
    filter_3 = df['weight'] >= df['weight'].quantile(0.025)
    filter_4 = df['weight'] <= df['weight'].quantile(0.975)
    filter = filter_1 & filter_2 & filter_3 & filter_4
    df_heat = df[filter]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))


    # 14
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, mask = mask, ax=ax, fmt='.1f', annot=True, cmap = 'coolwarm')

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig

print(draw_heat_map())