from streamlit_pills import pills
import json
import streamlit as st


def show_page():
    # Load technical skills data from the JSON file
    with open(r'data/technical_skills.json') as file:
        technical_skills = json.load(file)

    # Extract skill names and descriptions from the data
    skills = [skill["name"] for skill in technical_skills["skills"]]

    # Set up the layout: right_column for categories, left_column for descriptions
    right_column, left_column = st.columns([2, 1])

    with right_column:
        st.title("Technical Skills")
        # Use pills to let users select a category
        selected = pills("Select a category", skills)

    with left_column:
        st.title("Description")
        # Display the description for the selected skill
        for skill in technical_skills["skills"]:
            if selected == skill["name"]:
                st.markdown(f"**{skill['name']}:**")
                st.markdown(skill["description"])
