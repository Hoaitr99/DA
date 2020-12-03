import pandas as pd

dic = {
    'name':
        ['William', 'Emma', 'Sofia', 'Markus', 'Edward', 'Thomas', 'Ethan', 'Olivia', 'Arun', 'Anika', 'Paulo'],
    'region':
        ['East', 'North', 'East', 'South', 'West', 'West', 'South', 'West', 'West', 'East', 'South'],
    'sales':
        [50000, 52000, 90000, 34000, 42000, 72000, 49000, 55000, 67000, 65000, 67000],
    'expenses':
        [42000, 43000, 50000, 44000, 38000, 39000, 42000, 60000, 39000, 44000, 45000]}

df = pd.DataFrame(data=dic)
# print(df)
# print(df[df['region']=='East'])
# print(df[df['sales']> 50000])
# print(df.sort_values(by=['sales']))
# print(df.sort_values(by=['sales','expenses']))
# print(df.sort_values(by='sales', ascending=False))

df2 = pd.read_csv('database.csv')
# print(df2)
date_time_df = df2['Time'] + ' ' + df2['Date']
# print(df2.describe())

print(date_time_df.head(10))


print("-"*10,"Sau khi convert: ")



print(pd.to_datetime(date_time_df.head(10), format='%H:%M:%S  %m/%d/%Y'))
