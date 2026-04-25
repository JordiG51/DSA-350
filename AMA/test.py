import pandas as pd
import matplotlib.pyplot as plt
from Final import year_format, extract_birth_year

df_raw = pd.read_csv('alumni_anonymized.csv')

entries = []
for index, row in df_raw.iterrows():
    exit_yr = year_format(row['Custom.Year'])
    birth_yr = extract_birth_year(row['Places & Date of Birth & Death'])
    
    if exit_yr and birth_yr:
        entries.append({
            'ID': row['Id No'],
            'Last_Name': row['Name'],
            'Exit_Year': int(exit_yr),
            'Birth_Year': int(birth_yr)
        })

df = pd.DataFrame(entries)
df.set_index('ID', inplace=True)

df['Age_at_Exit'] = df['Exit_Year'] - df['Birth_Year']

df = df[(df['Age_at_Exit'] >= 7) & (df['Age_at_Exit'] <= 23)]

df.to_csv('alumni_clean.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['Exit_Year'], df['Age_at_Exit'], alpha=0.5, color='royalblue')
plt.title('Augusta Military Academy: Student Age Trends (1890–1960)')
plt.xlabel('Year of Departure')
plt.ylabel('Age at Exit')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
