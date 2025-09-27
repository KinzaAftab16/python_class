import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon=":lock:")

st.title("How Strong Is Your Password? Let’s Find Out! 🔍")
st.write("## Welcome to Your First Step Toward Stronger Security – Test Your Password Now! 🔐")
# st.write("---")
st.markdown("""
Test your password’s strength and improve your security in just a few clicks. Let’s make sure your passwords are as strong as possible! 🔐
""")


password = st.text_input("Enter Your Password", type="password")

feedback = []
score = 0

if password:
    if len(password) >=8 :
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Password should have at least one uppercase letter and one lowercase letter.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should have at least one digit.")
    
    if re.search(r"@$&!*", password):
        score += 1
    else:
         feedback.append("❌Password should have at least one special character.")
    
    if score == 4:
        st.success("🔒 Excellent! Your password is strong! You’ve met all the criteria for a secure password.")
    elif score == 3:
        st.warning("💪 Great! Your password is strong, but there's a little room for improvement.")
    else:
        st.error("😕 Weak password. This is not enough to secure your account.")

    if feedback:
        st.markdown('## Improvement Suggestion')
        for tip in feedback:
            st.write(tip)
else:
        st.info("Please enter a password to check its strength.")