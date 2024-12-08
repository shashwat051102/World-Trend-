import pandas as pd
import numpy as np


df = pd.read_csv('world-data-2023.csv')

df.drop('Abbreviation', axis=1, inplace=True)

transform = [ 'Agricultural Land( %)',  'Armed Forces size','Land Area(Km2)','Density\n(P/Km2)',
'Forested Area (%)', 'Co2-Emissions','CPI', 'CPI Change (%)', 'Gasoline Price', 'GDP',
'Gross primary education enrollment (%)','Gross tertiary education enrollment (%)',
'Minimum wage', 'Out of pocket health expenditure', 'Urban_population','Population: Labor force participation (%)',
'Population' ,'Tax revenue (%)', 'Unemployment rate','Total tax rate']
df[transform] = df[transform].map(lambda x: float(str(x).replace(',', '').replace('$', '').replace('%', '')))

df['Urban_percent'] = df['Urban_population'] / df['Population'] * 100

df['Agricultural Land(%)'] = pd.to_numeric(df['Agricultural Land( %)'], errors='coerce')

df['Country'] = df['Country'].str.replace("S�����������", "Sao Tome and Principe")

df['GDP_per_capita'] = (df['GDP'] / df['Population'])/1000
df['Co2_Emissions_per_person'] = df['Co2-Emissions'] / df['Population']

num_cols = df.select_dtypes(include=np.number).columns
cat_cols = df.select_dtypes(include='object').columns