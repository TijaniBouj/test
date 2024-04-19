import streamlit as st
import base64

# Path to the background image
bg_path = "bgg.png"
gif_url = "https://media2.giphy.com/media/kLano1oGCDDmlwttPh/giphy-downsized.gif"  # Replace with the URL of your GIF

# Set background image with zoom out effect
main_bg_ext = "bg"
main_bg = open(bg_path, "rb")
bg_encoded = base64.b64encode(main_bg.read()).decode()
st.markdown(
    f"""
    <style>
    .stApp {{
        background: url(data:image/{main_bg_ext};base64,{bg_encoded});
        background-size: contain; /* Zoom out effect */
        background-repeat: no-repeat;
        background-position: center;
    }}
    .gif-container {{
        position: absolute;
        top: 0;
        left: 0;
        margin-top: 90px; /* Adjust vertical position as needed */
        margin-left: 10px; /* Adjust horizontal position as needed */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Display GIF
st.markdown(
    f'<div class="gif-container"><img src="{gif_url}" width="120"></div>',
    unsafe_allow_html=True
)

# Main content (if any)
st.title("")  # Empty title
st.sidebar.success("Selected a page above.")  # Sidebar message
