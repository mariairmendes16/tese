import streamlit as st
import openai
import os

# Retrieve API key from environment variable
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

def generate_header(header_hotel_logo, header_menu, header_view_in_browser, branding_colors):
    response_header = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-0125:personal:tentativa18:96h7SJau",
      messages=[
        {"role": "system", "content": "Generate visually appealing HTML email headers, within a structured layout comprising just the email header, according to the user requirement provided."},
        {"role": "user","content": f"HOTEL LOGO: {header_hotel_logo}; MENU: {header_menu}; VIEW IN BROWSER LINK: {header_view_in_browser}; BRANDING COLORS: {branding_colors}"},
      ],
      temperature=0.4,
      max_tokens=4096,
      top_p=0.5,
    )
    return response_header.choices[0].message['content']

def generate_content(email_category, email_description, branding_colors):
    response_content = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-0125:personal:tentativa18:96h7SJau",
      messages=[
        {"role": "system",
          "content": "Generate visually appealing HTML email templates that encompass just the email content, catering to user specifications and ensuring a structured layout for optimal presentation and engagement. Never generate headers or footers."},
        {"role": "user", "content": f"EMAIL CATEGORY: {email_category} ; SMALL DESCRIPTION: {email_description}; BRANDING COLORS: {branding_colors}; ADDITIONAL NOTES: -"}
      ],
      temperature=0.6,
      max_tokens=4096,
      top_p=0.7,
    )
    return response_content.choices[0].message['content']

def generate_footer(footer_hotel_logo, footer_hotel_info, footer_menu, footer_social_media, footer_copyrighting_info, footer_unsubscribe_link, branding_colors):
    response_footer = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-0125:personal:tentativa18:96h7SJau",
      messages=[
        {"role": "system", "content": "Generate visually appealing HTML email footers, within a structured layout comprising just the email footer, according to the user requirement provided."},
        {"role": "user", "content": f"HOTEL LOGO: {footer_hotel_logo}; HOTEL INFORMATION: {footer_hotel_info}; MENU: {footer_menu}; SOCIAL MEDIA LINKS: {footer_social_media}; COPYRIGHTING INFORMATION: {footer_copyrighting_info}; UNSUBSCRIBE OPTION: {footer_unsubscribe_link}; BRANDING COLORS: {branding_colors}"}
      ],
      temperature=0.2,
      max_tokens=4096,
      top_p=0.4,
    )
    return response_footer.choices[0].message['content']

# Streamlit UI
st.title("AI Email Template Generator")

# Input fields
col1, col2 = st.columns(2)
with col1:
    st.header("Header")
    header_hotel_logo = st.checkbox("Header Hotel Logo")
    header_menu = st.checkbox("Header Menu")
    header_view_in_browser = st.checkbox("View in Browser Link")

with col2:
    st.header("Footer")
    footer_hotel_logo = st.checkbox("Footer Hotel Logo")
    footer_hotel_info = st.checkbox("Hotel Information")
    footer_menu = st.checkbox("Footer Menu")
    footer_social_media = st.checkbox("Social Media Links")
    footer_copyrighting_info = st.checkbox("Copyrighting Information")
    footer_unsubscribe_link = st.checkbox("Unsubscribe Link")

st.header("General Settings")
branding_colors = [st.color_picker("Branding Color 1"), st.color_picker("Branding Color 2"), st.color_picker("Branding Color 3")]
email_category = st.selectbox("Email Category", ["Apology","Birthday Email","Booking Cancellation","Booking Confirmation","Check-Out Reminder", "Double Opt-In", "F&B", "Feedback Request" , "Informative", "Invitation", "Invoice Email", "Legal Updates",  "Loyalty Offer", "Loyalty Program Presentation", "Mid-stay", "New Level of Loyalty Program", "New Loyalty Member", "Newsletter", "Pre-arrival",  "Spa", "Special Occasions", "Special Offers", "Stay Anniversary", "Welcome Email"])
speech_tone = st.selectbox("Speech Tone", ["🤝 Professional", "😊 Friendly", "🎉 Celebratory", "🙏 Apologetic", "💡 Informative", "🌟 Persuasive", "💌 Welcoming", "🥳 Excited", "🛎️ Urgent", "🤗 Appreciative"])
email_description = st.text_area("Small Description (Max 200 Characters)", max_chars=200)


# Generate email components
if st.button("Generate Email Template"):
    st.subheader("Header")
    header_output = generate_header(header_hotel_logo, header_menu, header_view_in_browser, branding_colors)
    st.write(header_output, unsafe_allow_html=True)  # Allow HTML rendering

    #st.subheader("Content")
    #content_output = generate_content(email_category, email_description, branding_colors)
    #st.write(content_output, unsafe_allow_html=True)  # Allow HTML rendering

    #st.subheader("Footer")
    #footer_output = generate_footer(footer_hotel_logo, footer_hotel_info, footer_menu, footer_social_media, footer_copyrighting_info, footer_unsubscribe_link, branding_colors)
    #st.write(footer_output, unsafe_allow_html=True)  # Allow HTML rendering
