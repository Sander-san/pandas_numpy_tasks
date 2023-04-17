import pandas as pd


adult = pd.read_csv('./data/adult.data.csv')


# Task 1
male_and_female_counts = adult['sex'].value_counts()


# Task 2
total_avg_age = round(adult['age'][adult['sex'] == 'Male'].mean())


# Task 3
total_people = adult['native-country'].count()
people_from_us = adult['native-country'][adult['native-country'] == 'United-States'].count()
other_people = adult['native-country'][adult['native-country'] != 'United-States'].count()
percent_from_total = round(people_from_us / total_people * 100)


# Task 4-5
avg_deviation_big_salary = adult['age'][adult['salary'] == '>50K'].std()
avg_deviation_small_salary = adult['age'][adult['salary'] == '<=50K'].std()


# Task 6
def check_education_lvl(data):
    people_with_big_salary = data['education'][adult['salary'] == '>50K'].isin(['Bachelors', 'Prof-school', 'Assoc-acdm',
                                                        'Assoc-voc', 'Masters', 'Doctorate']).describe()

    if people_with_big_salary['count'] == people_with_big_salary['freq']:
        return 'Absolute true'
    elif people_with_big_salary['top']:
        return 'Most people with big salary have a good education'
    else:
        return "It's false"


check_education_lvl(adult)


# Task 7
age_by_race_statistic = adult.groupby('race')['age'].describe()
oldest_pac_asian = adult['age'][adult['race'] == 'Asian-Pac-Islander'].max()


# Task 8
def which_man_earns_more(data):
    married_men = data['salary'][
              (data['sex'] == 'Male') &
              (data['salary'] == '>50K') &
              (data['marital-status'].isin(['Married-civ-spouse', 'Married-spouse-absent', ' Married-AF-spouse']))
          ].count()
    single_men = data['salary'][
              (data['sex'] == 'Male') &
              (data['salary'] == '>50K') &
              (~data['marital-status'].isin(['Married-civ-spouse', 'Married-spouse-absent', ' Married-AF-spouse']))
          ].count()

    if married_men > single_men:
        return f'Married men earns more'
    elif married_men == single_men:
        return f'Equal'
    else:
        return f'Single men earns more'


which_man_earns_more(adult)


# Task 9
def who_works_more(data):
    max_time = data['hours-per-week'].max()
    total = data['hours-per-week'][data['hours-per-week'] == max_time].count()
    with_big_salary = data['hours-per-week'][
        (data['hours-per-week'] == max_time) &
        (data['salary'] == '>50K')
    ].count()
    return f'Max available time per week - {max_time}\n' \
           f'The total number of people who work these hours - {total}\n' \
           f'People with big salary percent - {round(with_big_salary / total * 100)}%'


who_works_more(adult)


# Task 10
avg_work_hours_in_diff_countries = adult.groupby(['native-country', 'salary'])['hours-per-week'].mean()


# Task 11
adult.loc[(adult['age'] < 36), 'age-group'] = 'young'
adult.loc[(adult['age'] > 35) & (adult['age'] < 70), 'age-group'] = 'adult'
adult.loc[(adult['age'] > 69), 'age-group'] = 'retiree'


# Task 12-13
def salary_by_age_groups(data):
    y = adult['salary'][(adult['salary'] == '>50K') & (adult['age-group'] == 'young')].count()
    a = adult['salary'][(adult['salary'] == '>50K') & (adult['age-group'] == 'adult')].count()
    r = adult['salary'][(adult['salary'] == '>50K') & (adult['age-group'] == 'retiree')].count()

    m = max(y, a, r)
    if a == m:
        m = 'adult'
    elif y == m:
        m = 'young'
    else:
        m = 'retiree'

    return f'young - {y}\nadult - {a}\nretiree - {r}\nmost earn - {m}'


salary_by_age_groups(adult)
# groups = adult.groupby(['age-group', 'salary'])['salary'].count()


# Task 14
def filter_func(data):
    people_count_in_occupations = adult.groupby('occupation')['occupation'].count()
    avg_age_in_occupation = adult.groupby(['occupation'])[['age']].mean()

    return 'zalupa'


# print(filter_func(adult))






# to check data
test2 = adult['occupation']
print(f'All occupations - {test2.unique()}')
print(f'Total people - {21790 + 10771}')

# print(adult['occupation'][adult['hours-per-week'] > 5])
# print(adult['occupation'][adult['hours-per-week'] > 5].unique())  # same count as test2

