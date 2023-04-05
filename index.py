import openai
import streamlit as st

# Set OpenAI API key
openai.api_key = "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"

# Set up Streamlit app
st.set_page_config(page_title="Text Generator", page_icon=":pencil2:")
st.title("Text Generator")
st.image("header_image.png", use_column_width=True)

# Text prompt input field
prompt = st.text_area("Enter text prompt:", height=100)

# Generate text using the OpenAI API
if st.button("Generate Text"):
    with st.spinner("Generating text..."):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.9,
        )
        generated_text = response.choices[0].text
    
    # Display generated text
    st.subheader("Generated Text:")
    st.write(generated_text)

# Add bullet points to highlight key features


# Add social media share buttons

