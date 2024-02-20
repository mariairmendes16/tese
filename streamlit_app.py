import streamlit as st
from langchain import LangChain  # Assuming you have LangChain installed
from openai import OpenAI  # Assuming you have OpenAI API access

# Initialize LangChain and OpenAI API
langchain = LangChain()
openai_api = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# Streamlit app layout
st.title("HTML Email Template Generator")

# User inputs for header section
st.header("Header Section")
hotel_logotype = st.checkbox("Hotel Logotype")
menu = st.checkbox("Menu")
social_media_links = st.checkbox("Social Media Links")
view_in_browser_link = st.checkbox("View in Browser Link")

# User inputs for content section
st.header("Content Section")
email_category = st.selectbox("Email Category", [
    "Apology", "Birthday Email", "Booking Cancellation", "Booking Confirmation",
    "Check-Out Reminder", "Double Opt-In", "F&B", "Feedback Request",
    "Informative", "Invitation", "Invoice Email", "Legal Updates",
    "Loyalty Offer", "Loyalty Program Presentation", "Mid-stay",
    "New Level of Loyalty Program", "New Loyalty Member", "Newsletter",
    "Pre-arrival", "Spa", "Special Occasions", "Special Offers",
    "Stay Anniversary", "Welcome Email"
])
small_description = st.text_input("Small Description", max_chars=200)

# User inputs for footer section
st.header("Footer Section")
footer_hotel_logotype = st.checkbox("Hotel Logotype")
hotel_information = st.checkbox("Hotel Information")
footer_menu = st.checkbox("Menu")
footer_social_media_links = st.checkbox("Social Media Links")
copyrighting_information = st.checkbox("Copyrighting Information")

# General requirements
st.header("General Requirements")
additional_notes = st.text_input("Additional Notes", max_chars=100)
branding_colors = st.text_input("Branding Colors", "Color1; Color2; Color3")

# Button to generate HTML email template
if st.button("Generate HTML Email Template"):
    # Prepare input data for LangChain model
    input_data = {
        "header": {
            "hotel_logotype": hotel_logotype,
            "menu": menu,
            "social_media_links": social_media_links,
            "view_in_browser_link": view_in_browser_link
        },
        "content": {
            "email_category": email_category,
            "small_description": small_description
        },
        "footer": {
            "hotel_logotype": footer_hotel_logotype,
            "hotel_information": hotel_information,
            "menu": footer_menu,
            "social_media_links": footer_social_media_links,
            "copyrighting_information": copyrighting_information
        },
        "general_requirements": {
            "additional_notes": additional_notes,
            "branding_colors": branding_colors
        }
    }
    
    # Generate HTML email template using LangChain and OpenAI
    generated_template = langchain.generate(input_data, model=openai_api)
    
    # Display generated HTML email template
    st.write("Generated HTML Email Template:")
    st.code(generated_template)
