import pandas as pd
df = pd.read_csv(r'C:\Users\DELL\Downloads\Titanic.csv')

young_passengers = df.loc[df['Age'] < 35, 'Name']
print(young_passengers)

print(df.iloc[10:26, 3:6])

agg_stats = df[['Age', 'Fare']].agg(['count', 'mean', 'std', 'min', 'max'])
print(agg_stats)

fare_mean = df.groupby(['Sex', 'Pclass'])['Fare'].mean()
print(fare_mean)
