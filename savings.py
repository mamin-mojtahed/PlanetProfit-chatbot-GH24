import streamlit as st
from chatgpt import ask
import time

st.title("How can I help you today?")

# Input text box for user input
user_input = st.text_input("You:", placeholder="e.g. I am 21 years old, live in a low income neighbourhood, and work in manufacturing.")

# Button to send the message
if st.button("Ask") and user_input.strip() != "":
    with st.spinner("Loading..."):
        try:
            response = ask(user_input)
            ## TEST CODE: ##
            # time.sleep(1.5)
            # response = "test is 3454$ until eknkenf inio n 343$"
        except Exception as e:
            response = "Network Issue: " + str(e)

    # st.text_area("Bot:",
    #              response,
    #              height=(len(response) // 80 + len(response.split('\n')) + 1) * 20,
    #              disabled=True)
    response_md_cleaned = response.replace("$", "\$")
    st.markdown(f"""### Result:\n{response_md_cleaned}""")
