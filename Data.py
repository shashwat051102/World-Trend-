import streamlit as st
import feature as fe

df = fe.df

st.title("Top Ten list :trophy:")

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_unemployment = df.sort_values(by='Unemployment rate', ascending=False).reset_index(drop=True)
df_sorted_unemployment.index += 1

top_unemployment_countries = df_sorted_unemployment[['Country', 'Unemployment rate']].head(10)
st.markdown("### :chart_with_upwards_trend: Top 10 countries with highest Unemployment rate")

st.dataframe(top_unemployment_countries)

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_unemployment_asc = df.sort_values(by='Unemployment rate', ascending=True).reset_index(drop=True)
df_sorted_unemployment_asc.index += 1

top_unemployment_countries_asc = df_sorted_unemployment_asc[['Country', 'Unemployment rate']].head(10)
st.markdown("### :chart_with_downwards_trend: Top 10 countries with lowest Unemployment rate")

st.dataframe(top_unemployment_countries_asc)

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_per_capita_asc = df.sort_values(by='GDP_per_capita', ascending=True).reset_index(drop=True)
top_per_capita_countries_asc = df_sorted_per_capita_asc[['Country', 'GDP_per_capita']].head(10)
st.markdown("### :money_with_wings: Top 10 countries with lowest GDP per capita")
st.dataframe(top_per_capita_countries_asc)

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_per_capita_desc = df.sort_values(by='GDP_per_capita', ascending=False).reset_index(drop=True)
top_per_capita_countries_desc = df_sorted_per_capita_desc[['Country', 'GDP_per_capita']].head(10)
st.markdown("### :moneybag: Top 10 countries with Highest GDP per capita")
st.dataframe(top_per_capita_countries_desc)

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_Urban = df.sort_values(by='Urban_percent', ascending=False).reset_index(drop=True)
df_sorted_Urban.index += 1

top_Urban_pop = df_sorted_Urban[['Country', 'Urban_percent']].head(10)
st.markdown("### :cityscape: Top 10 countries with highest percent of population living in Urban areas")
st.dataframe(top_Urban_pop)

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_Urban_least = df.sort_values(by='Urban_percent', ascending=True).reset_index(drop=True)
df_sorted_Urban_least.index += 1

least_Urban_pop = df_sorted_Urban_least[['Country', 'Urban_percent']].head(10)
st.markdown("### :house_with_garden: Top 10 countries with lowest percent of population living in Urban areas")
st.dataframe(least_Urban_pop)

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_co2_asc = df.sort_values(by='Co2_Emissions_per_person', ascending=True).reset_index(drop=True)
top_co2_countries_asc = df_sorted_co2_asc[['Country', 'Co2_Emissions_per_person']].head(10)
st.markdown("### :earth_americas: Top 10 countries with lowest CO2 emissions per person")
st.dataframe(top_co2_countries_asc)

st.markdown('-----------------------------------------------------------------------------------')

df_sorted_co2_desc = df.sort_values(by='Co2_Emissions_per_person', ascending=False).reset_index(drop=True)
top_co2_countries_desc = df_sorted_co2_desc[['Country', 'Co2_Emissions_per_person']].head(10)
st.markdown("### :factory: Top 10 countries with highest CO2 emissions per person")
st.dataframe(top_co2_countries_desc)

st.markdown('-----------------------------------------------------------------------------------')
