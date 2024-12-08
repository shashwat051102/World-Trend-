import streamlit as st

st.sidebar.header("Navigation")

pg = st.navigation(pages=[
    st.Page(
        page="Home.py",
        title="Home",
        icon="🏠",
        default=True
    ),
    st.Page(
        page="Data.py",
        title="Data",
        icon="📊",
        # default = True
    ),
    st.Page(
        page="Charts.py",
        title="Charts",
        icon="📈",
    )
])
pg.run()
