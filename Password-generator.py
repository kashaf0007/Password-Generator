import re
import random
import string
import streamlit as st
st.markdown(
    """
    <style>
    .stApp {
        background-color:#f9ccca ;
    }
    </style>
    """,
    unsafe_allow_html=True
)
def check_password_strength(password):
    score = 0
    suggestions = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make the password at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", []
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", suggestions
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", suggestions

def generate_strong_password(length=8):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI

st.title("🔒 Password Strength Meter")
st.write("Enter your Password and check Security")
password = st.text_input("Enter your password", type="password")

if password:
    result, suggestions = check_password_strength(password)
    st.write(result)
    for suggestion in suggestions:
        st.write("-", suggestion)

    if st.button("Generate Strong Password"):
        strong_password = generate_strong_password()
        st.write("🔑 Suggested Strong Password:", strong_password)
st.write("Build with ❤️ by KASHAF AMAN")
