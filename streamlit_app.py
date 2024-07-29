import streamlit as st
from st_pages import Page, show_pages, add_page_title, hide_pages, Section
from chatgpt import ask

st.set_page_config(
    page_title="PlanetProfit",
    page_icon="✳️",
    menu_items={
        'About': "# Made by: Amin, Milind, Humza, Hussein - in GOODHack24"
    }
)

show_pages(
    [
        Page("streamlit_app.py", "Savings", "🌱"),
        Page("pages/community.py", "Community", "🌳")
    ]
)

col1t1,col2=st.columns(2)

st.sidebar.markdown("# ✳️ PlanetProfit")

# Variable to track the active tab
active_tab = st.session_state.get("active_tab", "Savings 🌱")

# Function to reset the session state
def reset_session_state():
    st.session_state["active_tab"] = "Savings 🌱"

# Chatbot
# Define a function to generate responses
def get_response(input_text):
    # Simple echo bot
    return f"Echo: {input_text}"

# Content of tab 1 (Savings 🌱)
if active_tab == "Savings 🌱":
    st.title("How can I help you today?")

    # Input text box for user input
    user_input = st.text_input("You:", placeholder="e.g. I am 21 years old, live in a low income neighbourhood and work in manufacturing.")

    # Button to send the message
    if st.button("Send"):
        if user_input.strip() != "":
            response = ask(user_input)
            # response = "test"

            # st.text_area("Bot:",
            #              response,
            #              height=(len(response) // 80 + len(response.split('\n')) + 1) * 20,
            #              disabled=True)
            st.markdown(f"""### Result:\n{response}""")
            
            
#             response = f"""Based on your details, here are the top 5 climate and sustainability programs in Kitchener City that you might be eligible for and how they can help you save money:

# 1. Low-Income Energy Assistance Program (LIEAP):
#    - Description: This program helps low-income households by covering a portion of their heating costs.
#    - Benefit: You can save up to $650 for non-electric heating or up to $780 for electric heating on your energy bills.
#    - Eligibility: Low-income residents of Ontario, with specific income thresholds that vary depending on household size and location.
#    - How to Apply: Contact your local electricity provider for details on income eligibility and the application process.

# 2. Ontario Electricity Support Program (OESP):
#    - Description: Provides financial assistance on electricity bills for low-income households.
#    - Benefit: Reduction in your monthly electricity bill, with the amount depending on your income level and household size.
#    - Eligibility: Low-income residents of Ontario.
#    - How to Apply: You need to contact your local electricity provider to check your eligibility and to apply.

# 3. Community Development Infrastructure Program (CDIP):
#    - Description: Offers grants up to $10,000 for community development projects in Kitchener.
#    - Benefit: Financial support for a project that can improve your neighborhood, potentially increasing property values and quality of life.
#    - Eligibility: Groups such as neighborhood associations or communities of interest in a geographic area of Kitchener.
#    - How to Apply: You would need to be part of a group with an organizational structure to apply.

# 4. Green Industrial Facilities and Manufacturing Program:
#    - Description: Provides financial assistance to industrial facilities and manufacturers to implement energy-efficient solutions.
#    - Benefit: Could potentially reduce your workplace's operational costs through energy savings, possibly affecting employment stability and growth.
#    - Eligibility: Industrial facilities and manufacturers in Canada looking to improve energy efficiency.
#    - How to Apply: Specific application procedures would likely be detailed on the program's official website or through industry channels.

# 5. Canada Greener Homes Loan:
#    - Description: Offers interest-free loans to homeowners to make energy-efficient upgrades.
#    - Benefit: Although you're not a homeowner, knowing about this program can be beneficial if your housing situation changes, or it might be relevant for friends and family. Loans can help finance significant energy-efficient renovations, reducing long-term living costs.
#    - Eligibility: Canadian homeowners.
#    - How to Apply: You would apply through the program's official website or government service outlets.

# These programs can help reduce your living and working costs through energy savings and direct financial assistance, improving both your immediate financial situation and contributing to long-term sustainability in your community.
#                                 """
            

