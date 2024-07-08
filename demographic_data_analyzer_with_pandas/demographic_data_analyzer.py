import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('demographic_data_analyzer_with_pandas/adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    df_men = df[df['sex'] == 'Male']
    average_age_men = round(df_men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_ed = (len(df['education']))
    total_high_ed = len(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])
    percentage_bachelors = (round(((len(df[df['education'] == 'Bachelors']))/total_ed) * 100, 1))

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    
    advanced_ed_and_50k = (df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')
    no_advanced_ed_and_50k = (~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')

    higher_education = len(df[advanced_ed_and_50k])
    lower_education = len(df[no_advanced_ed_and_50k])

    # percentage with salary >50K
    higher_education_rich = round((higher_education/total_high_ed) * 100, 1)
    lower_education_rich = round((lower_education/(total_ed - total_high_ed)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    total_min_hours = (df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(total_min_hours)

    rich_percentage = round((num_min_workers / total_ed) * 10, 1)

    # What country has the highest percentage of people that earn >50K?
    salary_count = df.loc[df['salary'] == '>50K']
    og_df = salary_count['native-country'].value_counts()
    new_df = df[['native-country','salary']]
    new_df_count = new_df['native-country'].value_counts()
    percentage = og_df / new_df_count
    highest_earning_country = percentage.idxmax()
    highest_earning_country_percentage = round(percentage.max() * 100, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    a = (df['salary'] == '>50K') & (df['native-country'] == 'India')
    a_1 = df[a]['occupation']
    a_2 = a_1.value_counts()
    top_IN_occupation = a_2.idxmax()


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
