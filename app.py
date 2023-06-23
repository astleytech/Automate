import streamlit as st
import docx
import openai
import os

# Set up the OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Create the Streamlit app
st.title("Text Summarization Tool")

# Create the file upload widget
file = st.file_uploader("Upload Word document", type=["docx"])

# Create the prompt input widgets
prompts = []
num_prompts = st.number_input("Number of prompts", min_value=1, max_value=10, step=1)
for i in range(num_prompts):
    prompt = st.text_input(f"Prompt {i+1}")
    prompts.append(prompt)

# Process the file and generate summaries
if file is not None:
    # Read the text from the Word document
    doc = docx.Document(file)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])

    # Generate summaries for each prompt
    summaries = []
    for prompt in prompts:
        prompt_text = f"{prompt}\n\n{text}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_text,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        summary = response.choices[0].text.strip()
        summaries.append(summary)

    # Display the summaries
    for summary in summaries:
        st.bullet(summary)