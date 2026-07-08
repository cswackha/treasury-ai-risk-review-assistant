import streamlit as st

st.set_page_config(page_title="Treasury AI Risk Review Assistant")

st.title("Treasury AI Risk & Use Case Review Assistant")

st.write("This prototype evaluates proposed AI use cases for risk, controls, and deployment readiness.")

use_case = st.text_area("Describe the AI use case")

if st.button("Generate Review"):
    if use_case.strip():
        st.subheader("Prototype Review")
        st.write("Risk Level: Medium")
        st.write("Recommended Controls: Human review, logging, access control, cybersecurity review, and test validation before production.")
    else:
        st.warning("Please enter an AI use case.")