#import libraries required
from openai import OpenAI

import streamlit as st
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

st.header("Transform Your text to Images")
Image_Text=st.text_area("Enter your text messages to convert into a Image")
if st.button("Generate"):
    response = client.images.generate(
    model="dall-e-3",
    prompt=Image_Text,
    size="1024x1024",
    quality="standard",
    n=1,
    )
    image_url = response.data[0].url
    print(image_url)
    st.info(image_url)
else:
    st.warning("Add your text to Generate")