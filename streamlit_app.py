import streamlit as st
import openai
from bs4 import BeautifulSoup

# Retrieve API key from environment variable
#openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_header(header_hotel_logo, header_menu, header_view_in_browser, branding_colors):
    response_header = openai.ChatCompletion.create(
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
    st.header('Header', divider=True)
    header_hotel_logo = st.checkbox("Header Hotel Logo")
    header_menu = st.checkbox("Header Menu")
    header_view_in_browser = st.checkbox("View in Browser Link")

with col2:
    st.header('Footer', divider=True)
    footer_hotel_logo = st.checkbox("Footer Hotel Logo")
    footer_hotel_info = st.checkbox("Hotel Information")
    footer_menu = st.checkbox("Footer Menu")
    footer_social_media = st.checkbox("Social Media Links")
    footer_copyrighting_info = st.checkbox("Copyrighting Information")
    footer_unsubscribe_link = st.checkbox("Unsubscribe Link")

st.header("General Settings", divider='grey')
col1, col2 = st.columns(2)
with col1:
    branding_colors = [st.color_picker("Branding Color 1"), st.color_picker("Branding Color 2"), st.color_picker("Branding Color 3")]

with col2:
    email_category = st.selectbox("Email Category", ["Apology","Birthday Email","Booking Cancellation","Booking Confirmation","Check-Out Reminder", "Double Opt-In", "F&B", "Feedback Request" , "Informative", "Invitation", "Invoice Email", "Legal Updates",  "Loyalty Offer", "Loyalty Program Presentation", "Mid-stay", "New Level of Loyalty Program", "New Loyalty Member", "Newsletter", "Pre-arrival",  "Spa", "Special Occasions", "Special Offers", "Stay Anniversary", "Welcome Email"])
    speech_tone = st.selectbox("Speech Tone", ["🤝 Professional", "😊 Friendly", "🎉 Celebratory", "🙏 Apologetic", "💡 Informative", "🌟 Persuasive", "💌 Welcoming", "🥳 Excited", "🛎️ Urgent", "🤗 Appreciative"])
email_description = st.text_area("Small Description (Max 200 Characters)", max_chars=200)


# Generate email components
#if st.button("Generate Email Template"):
    #st.subheader("Header")
    #header_output = generate_header(header_hotel_logo, header_menu, header_view_in_browser, branding_colors)
    #st.write(header_output)
    #st.write (header_output, unsafe_allow_html=True) # Allow HTML rendering

    #st.subheader("Content")
    #content_output = generate_content(email_category, email_description, branding_colors)
    #st.write(content_output, unsafe_allow_html=True)  # Allow HTML rendering

    #st.subheader("Footer")
    #footer_output = generate_footer(footer_hotel_logo, footer_hotel_info, footer_menu, footer_social_media, footer_copyrighting_info, footer_unsubscribe_link, branding_colors)
    #st.write(footer_output, unsafe_allow_html=True)  # Allow HTML rendering


if st.button("Generate Email Template"):
    st.subheader("Generated Template", divider='grey')
    generated_header = generate_header(header_hotel_logo, header_menu, header_view_in_browser, branding_colors)
    #generated_content = generate_content(email_category, email_description, branding_colors)
    #generated_footer = generate_footer(footer_hotel_logo, footer_hotel_info, footer_menu, footer_social_media, footer_copyrighting_info, footer_unsubscribe_link, branding_colors)
    
    # Parse the HTML Empty Template
    empty_template = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> <html dir="ltr" xmlns="http://www.w3.org/1999/xhtml" xmlns:o="urn:schemas-microsoft-com:office:office"> <head> <meta charset="UTF-8"> <meta content="width=device-width, initial-scale=1" name="viewport"> <meta name="x-apple-disable-message-reformatting"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta content="telephone=no" name="format-detection"> <title></title> <!--[if (mso 16)]> <style type="text/css"> a {text-decoration: none;} </style> <![endif]--> <!--[if gte mso 9]><style>sup { font-size: 100% !important; }</style><![endif]--> <!--[if gte mso 9]> <xml> <o:OfficeDocumentSettings> <o:AllowPNG></o:AllowPNG> <o:PixelsPerInch>96</o:PixelsPerInch> </o:OfficeDocumentSettings> </xml> <![endif]--> </head> <body> <div dir="ltr" class="es-wrapper-color"> <!--[if gte mso 9]> <v:background xmlns:v="urn:schemas-microsoft-com:vml" fill="t"> <v:fill type="tile" color="#f6f6f6"></v:fill> </v:background> <![endif]--> <table class="es-wrapper" width="100%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td class="esd-email-paddings" valign="top"> <table class="esd-header-popover es-header" cellspacing="0" cellpadding="0" align="center"> <tbody> <tr> <td class="esd-stripe" align="center"> <table class="es-header-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center"> <tbody> <tr> <td class="es-p20t es-p20r es-p20l esd-structure" align="left"> <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="180" valign="top"><![endif]--> <table class="es-left" cellspacing="0" cellpadding="0" align="left"> <tbody> <tr> <td class="es-m-p0r es-m-p20b esd-container-frame" width="180" valign="top" align="center"> <table width="100%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td class="esd-empty-container" style="display: none;" align="center"></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <!--[if mso]></td><td width="20"></td><td width="360" valign="top"><![endif]--> <table class="es-right" cellspacing="0" cellpadding="0" align="right"> <tbody> <tr> <td class="esd-container-frame" width="360" align="left"> <table width="100%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td class="esd-empty-container" style="display: none;" align="center"></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <!--[if mso]></td></tr></table><![endif]--> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <table class="es-content" cellspacing="0" cellpadding="0" align="center"> <tbody> <tr> <td class="esd-stripe" align="center"> <table class="es-content-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center"> <tbody> <tr> <td class="es-p20t es-p20r es-p20l esd-structure" align="left"> <table width="100%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td class="esd-container-frame" width="560" valign="top" align="center"> <table width="100%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td class="esd-empty-container" style="display: none;" align="center"></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <table class="esd-footer-popover es-footer" cellspacing="0" cellpadding="0" align="center"> <tbody> <tr> <td class="esd-stripe" align="center"> <table class="es-footer-body" width="600" cellspacing="0" cellpadding="0" bgcolor="#ffffff" align="center"> <tbody> <tr> <td class="esd-structure es-p20t es-p20b es-p20r es-p20l" align="left"> <!--[if mso]><table width="560" cellpadding="0" cellspacing="0"><tr><td width="270" valign="top"><![endif]--> <table class="es-left" cellspacing="0" cellpadding="0" align="left"> <tbody> <tr> <td class="es-m-p20b esd-container-frame" width="270" align="left"> <table width="100%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td class="esd-empty-container" style="display: none;" align="center"></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <!--[if mso]></td><td width="20"></td><td width="270" valign="top"><![endif]--> <table class="es-right" cellspacing="0" cellpadding="0" align="right"> <tbody> <tr> <td class="esd-container-frame" width="270" align="left"> <table width="100%" cellspacing="0" cellpadding="0"> <tbody> <tr> <td class="esd-empty-container" style="display: none;" align="center"></td> </tr> </tbody> </table> </td> </tr> </tbody> </table> <!--[if mso]></td></tr></table><![endif]--> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </td> </tr> </tbody> </table> </div> </body> </html>"""
    soup = BeautifulSoup(empty_template, 'html.parser')

    # Find all occurrences of elements with the class 'esd-stripe'
    esd_stripe_elements = soup.find_all(class_='esd-stripe')

    # Select the first occurrence - Header
    first_esd_stripe = esd_stripe_elements[0]
    first_esd_stripe.replace_with(BeautifulSoup(generated_header, 'html.parser'))

    # Select the second occurrence - Content
    #second_esd_stripe = esd_stripe_elements[1]
    #second_esd_stripe.replace_with(BeautifulSoup(generated_content, 'html.parser'))

    # Select the third occurrence - Footer
    #third_esd_stripe = esd_stripe_elements[2]
    #third_esd_stripe.replace_with(BeautifulSoup(generated_footer, 'html.parser'))

    # Convert the populated HTML template to a string
    populated_template = soup.prettify()

    # Display the populated HTML template in Streamlit
    st.write(populated_template, unsafe_allow_html=True)
    st.subheader('Generated HTML', divider='grey')
    st.write(populated_template)

