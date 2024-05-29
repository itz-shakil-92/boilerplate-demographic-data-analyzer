import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
        # Load the dataset
    df = pd.read_csv('/workspace/boilerplate-demographic-data-analyzer/adult.data.csv')

    # Filter out non-numeric ages
    non_numeric_ages = df[~df['age'].astype(str).str.isdigit()]
    if not non_numeric_ages.empty:
        print("Non-numeric ages found:")
        print(non_numeric_ages)
        # You can handle non-numeric values here, e.g., drop them or convert if possible
        df = df[df['age'].apply(lambda x: x.isnumeric())]


   # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    # Convert 'age' column to numeric
    df['age'] = pd.to_numeric(df['age'])

    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Percentage with Bachelors degrees
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Advanced education
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Percentage with higher education earning >50K
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / higher_education.sum()) * 100, 1)

    # Percentage without higher education earning >50K
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / lower_education.sum()) * 100, 1)

    # Min work time
    min_work_hours = df['hours-per-week'].min()

    # Percentage of rich among those who work the fewest hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = round((df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100, 1)

    # Country with highest percentage of rich
    rich_countries = df[df['salary'] == '>50K']['native-country'].value_counts()
    countries = df['native-country'].value_counts()
    highest_earning_country = (rich_countries / countries).idxmax()
    highest_earning_country_percentage = round((rich_countries / countries).max() * 100, 1)

    # Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:", higher_education_rich)
        print("Percentage without higher education that earn >50K:", lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work fewest hours:", rich_percentage)
        print("Country with highest percentage of rich:", highest_earning_country)
        print("Highest percentage of rich people in country:", highest_earning_country_percentage)
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
