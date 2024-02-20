import streamlit as st
import openai

# Set your OpenAI API key here
OPENAI_API_KEY = None  # Replace None with your API key

# Check if API key is provided
if OPENAI_API_KEY is None:
    st.error("Please provide your OpenAI API key.")
else:
    # Initialize OpenAI API client
    openai.api_key = OPENAI_API_KEY

    # Define a function to generate text using the OpenAI API
    def generate_text(prompt, max_tokens=50):
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

    # Streamlit app
    st.title("OpenAI API Demo")

    # Input for user prompt
    prompt = st.text_area("Enter your prompt:")

    # Generate button
    if st.button("Generate Text"):
        if prompt:
            # Generate text using OpenAI API
            with st.spinner("Generating..."):
                generated_text = generate_text(prompt)
            st.success("Text generated successfully:")
            st.write(generated_text)
        else:
            st.error("Please enter a prompt.")
