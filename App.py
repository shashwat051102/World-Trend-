import streamlit as st

st.sidebar.header("Navigation")

pg = st.navigation(pages=[
    st.Page(
        page="Pages/Home.py",
        title="Home",
        icon="🏠",
        default=True
    ),
    st.Page(
        page="Pages/Data.py",
        title="Data",
        icon="📊",
        # default = True
    ),
    st.Page(
        page="Pages/Charts.py",
        title="Charts",
        icon="📈",
    )
])
pg.run()
