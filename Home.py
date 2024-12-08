import streamlit as st

# Title and Introduction
st.title("🌍 World Data 2023 Report")
st.markdown("------------------------------------------------------------------")
st.markdown('### 🌐 Introduction')
st.markdown("""
This report provides an analysis of various socio-economic indicators for countries around the world in 2023. 
The data includes metrics such as:
- **GDP per capita**
- **Unemployment rate**
- **Urban population percentage**
- **CO2 emissions per person**
- And more...
""")

st.markdown("------------------------------------------------------------------")

# About Dataset
st.markdown('### :bar_chart: About Dataset')
st.markdown("""
The data was collected in **2023** and provides a comprehensive snapshot of the socio-economic landscape of the world at that time.
You can also explore the data interactively using various visualization tools provided in this report.
The dataset is available for download from the [World Bank Open Data](https://data.worldbank.org/) portal. 

**Metrics Included**:
- **Data Source**: World Bank
- **Number of Countries**: 217
- **Time Period**: 2023
""")

st.markdown("------------------------------------------------------------------")

# Data Analysis
st.markdown("### 📊 Data Analysis and Visualization")
st.markdown("""
In this section, we provide a detailed analysis of the socio-economic indicators using various charts and visualizations.

1. **GDP per Capita**:
    - We used a bar chart to compare the GDP per capita of different countries. This helps in understanding the economic standing of each country relative to others.
    - The top 10 countries with the highest GDP per capita are highlighted for a clearer perspective.

2. **Unemployment Rate**:
    - A line chart was used to show the trend of unemployment rates over the year 2023. This visualization helps in identifying any significant changes or patterns in employment.

3. **Urban Population Percentage**:
    - A pie chart was utilized to depict the distribution of urban population across various regions. This provides insights into the urbanization levels of different parts of the world.

4. **CO2 Emissions per Person**:
    - A scatter plot was created to analyze the relationship between GDP per capita and CO2 emissions per person. This helps in understanding the environmental impact of economic activities.

5. **Other Indicators**:
    - Additional charts and graphs were used to analyze other important indicators such as literacy rates, life expectancy, and access to clean water.

Each visualization is accompanied by a brief explanation to help interpret the data and understand the key takeaways.
""")



