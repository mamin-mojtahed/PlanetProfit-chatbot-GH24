import streamlit as st
from st_pages import Page, add_page_title, hide_pages, Section
from chatgpt import ask

st.set_page_config(
    page_title="PlanetProfit",
    page_icon="✳️",
    menu_items={
        'About': "# Made by: Amin, Milind, Humza, Hussein - in GOODHack24"
    }
)

# DYSFUNCTIONAL
# show_pages(
#     [
#         Page("streamlit_app.py", "Savings", "🌱"),
#         Page("pages/community.py", "Community", "🌳")
#     ]
# )

col1t1,col2=st.columns(2)

st.sidebar.markdown("# ✳️ PlanetProfit")

p1 = st.Page("savings.py", title="Savings", icon="🌱")
p2 = st.Page("community.py", title="Community", icon="🌳")
p3 = st.Page("calculator.py", title="Calculator", icon="☘️")

pg = st.navigation([p1, p2, p3])
pg.run()
