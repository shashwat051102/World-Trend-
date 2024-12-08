import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import feature as fe
import streamlit as st

st.title("📊 Charts")

st.markdown("--------------------------------------------------------------------------------")


non_positive_mask = fe.df['Tax revenue (%)'] <= 0

if non_positive_mask.any():
    df = fe.df[~non_positive_mask]
fig = px.scatter(df, x="Tax revenue (%)", y="Total tax rate",
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Dependency of tax revenue on tax rate",hover_name="Country")
# fig.show()

st.markdown("### 📈 1. Dependency of tax revenue on tax rate")
st.markdown('With this graph we can come to a conclusion that tax revenue is not dependent on tax rate')
st.plotly_chart(fig)

st.markdown("--------------------------------------------------------------------------------")

st.markdown("### 👶 2. Maternal mortality rate dependency on infant mortality rate")
st.markdown('This graphs shows that the death of both mother and child are codependent.')

fig1 = px.scatter(df, x="Infant mortality", y="Maternal mortality ratio",
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Maternal mortality rate dependency on infant mortality rate",hover_name="Country")

st.plotly_chart(fig1)

st.markdown("--------------------------------------------------------------------------------")

st.markdown("### 💰 3. Do high income means less infant mortality?")
st.markdown('As we can see from the graph that as the society earns more people tend to have better health infrastructure and thus have better treatment and care for mother and infant thus having less death.')

fig2 = px.scatter(df, x="GDP_per_capita", y="Infant mortality",
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Do high income means less infant mortality?",hover_name="Country")

st.plotly_chart(fig2)

st.markdown("--------------------------------------------------------------------------------")

st.markdown("### 💵 4. Can we buy life with money?")
st.markdown('Its same as infant mortality vs GDP per capita people with money have better life style, eating habits, health infrastructure and better condition to live in.')

fig3 = px.scatter(df, x="GDP_per_capita", y="Life expectancy",
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="can we buy life with money?",hover_name="Country")

st.plotly_chart(fig3)

st.markdown("--------------------------------------------------------------------------------")

st.markdown("### 🎓 5. Dependency of infant mortality on parents education")
st.markdown('As the society get educated primarily advanced education they tend to get more aware about practices to take care of mother during pregnanncy and what to do to take care of child after birth like all the vaccines required and dietry habits.')

fig4 = px.scatter(df, x="Gross tertiary education enrollment (%)", y="Infant mortality",
                 trendline="ols", trendline_options=dict(log_x=True),
                 title="Is infants life is dependent on there parents tertiary education?",hover_name="Country")

st.plotly_chart(fig4)

st.markdown("--------------------------------------------------------------------------------")

st.markdown("### 🌍 6. Life Expectancy By Country")
st.markdown('From this we can come to a conclusion that African countries are lagging behind rest of the world and thats why have the worst life expectancy compared to other countries and American and European Countries have best life Expectancy')

fig5 = px.choropleth(df, 
                    locations="Country", 
                    locationmode="country names", 
                    color="Life expectancy",
                    hover_name="Country", 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Life Expectancy by Country")

st.plotly_chart(fig5)

st.markdown("--------------------------------------------------------------------------------")

st.markdown("### 🌿 7. CO2 - Emission By Country ")
st.markdown('The big two have the highest co2 emission rate and The developing countries like India should take note and focus on more sustainable growth.')

fig6 = px.choropleth(df, 
                    locations="Country", 
                    locationmode="country names", 
                    color="Co2-Emissions",
                    hover_name="Country", 
                    color_continuous_scale=px.colors.sequential.Plasma,
                    title="Co2-Emissions by Country")
st.plotly_chart(fig6)
