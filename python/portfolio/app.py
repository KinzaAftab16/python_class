
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Portfolio", page_icon=":computer:", layout="wide")

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding =load_lottie("https://lottie.host/57d2a464-7df3-4587-8754-ab7b2b781010/BQ7oYiAFDJ.json")

with st.container():
    st.subheader("Hello! I'm Kinza Aftab :wave:")
    st.title("Frontend Developer.")
    st.write("Passionate web developer skilled in modern web technologies, creating user-friendly and responsive digital experiences.")
    st.write("[Learn more about me >] (https://kinzaaftab-portfolio.vercel.app/)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do?")
        # st.write("##")
        st.write(
            """
           - Develop responsive and high-performance websites and web applications

           - Utilize modern technologies including HTML, CSS, JavaScript, TypeScript, and Next.js

           - Focus on clean, maintainable code and scalable architecture

           - Prioritize user experience and performance optimization

           - Continuously learn and adapt to new tools and technologies
            """
        )
        with right_column:
            st_lottie(lottie_coding, height=300, key="Coding")



            # second section
    with st.container():
        st.write("---")
        st.header("Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.write("heloo")
        with text_column:
            st.subheader(" Hair Lounge – Salon Website")
            st.write("Description: A stylish and fully responsive website for a salon business. Includes services, gallery, about us, and a booking CTA.")
            st.write("**Tech Stack**: HTML, CSS, JavaScript, Font Awesome")

            st.subheader(". Dev Blog – Dynamic Blog with Sanity & Next.js")
            st.write("Description: A dynamic blog site where users can browse multiple posts and see full content pages.")
            st.write("**Tech Stack**:Next.js, Sanity CMS, Tailwind CSS")