import streamlit as st


def show_page():
    st.title("About Me")
    st.write("I'm Hongmei, a passionate Machine Learning and AI engineer.")


# Define the left and right columns
right_column, left_column = st.columns([1, 2])
with right_column:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(r"images/profile.png", use_column_width=True)

with left_column:
    st.title("About Me")
    st.markdown(
        "<div style='text-align: justify'>"
        "Hello! I'm Hongmei Jian Roy, and I'm absolutely passionate about artificial intelligence. The ever-evolving field of AI captivates me, not just as a career path but as a fascinating journey into the future."
        "<br>"
        "Witnessing AI transform industries, enhance everyday life, and solve complex problems is a constant source of inspiration."
        "<br>"
        "My skillset spans various areas, including machine learning, natural language processing, and computer vision. Proficient in programming languages such as Python and Java, I also have hands-on experience with frameworks like TensorFlow and PyTorch."
        "<br>"
        "Whether developing intelligent algorithms or fine-tuning models, I thrive on tackling challenging projects and pushing the boundaries of what's possible with AI. I'm a lifelong learner, with a curious mind, a love for tech, and a relentless drive to broaden my horizons and fuel my creativity.."
        "<br>"
        "Beyond the world of tech, I have a few hobbies that keep my life balanced and exciting. I enjoy walking in the mountains and by lakes, as it provides a refreshing break from the screen and a chance to connect with nature."
        "<br>"
        "Listening to music and dancing with the flow are integral parts of my life. My interests also extend to fashion, Eastern medicine, and ancient philosophy, which I find endlessly fascinating."
        "<br>"
        "Feel free to reach out if you'd like to chat more about AI, share insights, or even recommend a good book or hiking trail!"
        "<br>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://www.linkedin.com/in/hongmei-jian-roy-ab35471b0'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/homemadejam16'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:homemadejam16@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
