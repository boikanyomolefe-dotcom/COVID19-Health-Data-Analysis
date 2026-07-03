import pandas as pd
import openpyxl
from datetime import datetime

df = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/data-science-in-health-care-basic-statistical-analysis/COVID_19.xlsx',
    'Sheet1')

def parse(x):
    y=x.split()
    t=y[1][:8]
    z=y[0]+" "+t
    d=datetime.strptime(z,'%Y-%m-%d %H:%M:%S')
    return d

df = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/data-science-in-health-care-basic-statistical-analysis/COVID_19.xlsx',
    'Sheet1',na_values="NaN")
df = df.set_index('Date time')
df = df.reset_index()

print(df)

df = df.dropna(subset=['Gender'])
d = {'No' : False, 'Yes' : True}
c = 'Do you vaccinated influenza?'

df[c] = df[c].astype(object)
           
df.loc[:, c] = df[c].map(d)

print(df.shape)

df.info()
c = 'Age'
df[c] = df[c].astype('category')

df['Age']

for c in df.columns[1:-1]:
    df[c] = df[c].apply(lambda x : str(x) if str(x).find('(') == -1 else str(x)[:str(x).find('(')] ).astype('category')

df.info()

df.describe()

df.describe(include=['category'])

df['Age'].value_counts()

df.sort_values(by='Age', 
        ascending=True)

df.sort_values(by=['Age', 'Gender'], ascending=[True, False]).head()

df['Gender'].value_counts()

df['Gender'].value_counts().keys()

df[df['Gender'] == 'Female ']['Maximum body temperature'].mean()

df[(df['Gender'] == 'Male ') & (df['Do you smoke?'] == 'Yes') & (df['Have you had Covid`19 this year?'] == 'Yes')]['Maximum body temperature'].max()

df.groupby(['Gender'])['Maximum body temperature'].describe()

pd.crosstab(df['Age'], df['Gender'])

print(pd.pivot_table(df, values= 'Maximum body temperature', index= ['Age'], columns=['Gender'], aggfunc='mean', margins=True))


import matplotlib.pyplot as plt
import seaborn as sns

df['IgM level'] = pd.to_numeric(df['IgM level'], errors='coerce')

plt.figure()
sns.countplot(x='Age', hue='Gender', data=df)

plt.figure()
df.set_index('Date time')['Maximum body temperature'].resample('1D').sum().plot()

_, axes = plt.subplots(1, 2, sharey=True, figsize=(16,6))

df_t = df[df['Have you had Covid`19 this year?'] == 'Yes'].dropna(subset=['Maximum body temperature'])
sns.histplot(df_t['Maximum body temperature'], ax=axes[0], kde=True)

df_t = df[df['Have you had Covid`19 this year?'] == 'Maybe'].dropna(subset=['Maximum body temperature'])
sns.histplot(df_t['Maximum body temperature'], ax=axes[1], kde=True)

plt.show()

df =df[df['Age']!= 'nan']
df['Age'] = df['Age'].cat.remove_unused_categories() 
       
cols = ['Maximum body temperature', 'Maximum body temperature']
_, axes = plt.subplots(1, 2, sharey=True, figsize=(16,6))
sns.boxplot(y = df["Age"], x=df["Maximum body temperature"], ax=axes[0])
sns.violinplot(y = df["Age"], x=df["Maximum body temperature"],ax=axes[1] )


plt.show()

plt.savefig('boxplot_violin.png')
