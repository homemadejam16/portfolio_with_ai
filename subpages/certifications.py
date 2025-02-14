

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

def show_page():
    st.title("Certifications")
    # Certifications section
    st.header("📜 Certifications")

    # Creating a dataframe for certifications
    certifications_data = {
    "Vendor": ["Microsoft", "Microsoft", "NoShitSecurity", "Great Learning", "Splunk", "AttackIQ", "Coursera", "Try Hack Me", "Cybrary", "Google"],
    "Series": ["AZ-500 Azure Security Engineer", "AZ-900 Azure Fundamentals", "Azure Security Bootcamp", "Cloud Fundamentals", "Basic of Splunk", "Foundational and operationalizing Mitre Att&ack", "HTML, CSS, and JavaScript for Web Developers", "Advent of Cyber 3", "Introduction to IT and Cybersecurity", "Google Cloud Engineering Track"],
    "Awarded": ["Aug/2023", "Oct/2022", "July/2022", "June/2022", "May/2022", "May/2022", "Feb/2022", "Dec/2021", "Nov/2021", "Oct/2021"],
    "Expiration": ["Aug/2024", "Never", "Never", "Never", "Never", "Never", "Never", "Never", "Never", "Never"]
    }

    certifications_df = pd.DataFrame(certifications_data)
    st.table(certifications_df)

