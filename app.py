import streamlit as st
from stry_gen import generate_story_from_images, narrate_story
from PIL import Image

st.title("AI Story Generator From Images") #title
st.markdown("You can upload 1 to 10 images, choose an style and let AI write and narrate an story for you!")


with st.sidebar:
    st.header("Controls")


    #sidebar option to upload images
    uploaded_files = st.file_uploader(
        "upload your images here...",
        type=["png","jpg", "jpeg"],
        accept_multiple_files=True
    )

    #selcting an story style
    story_style= st.selectbox(
        "Pick a story style you'd like",
        ("Comedy", "Thriller", "Fairytale", "Sci-Fi", "Mystery", "Adventure", "Morale", "sarcastic brainrot")
    )

    #button to generate story
    generate_button= st.button("Generate Story and Narration", type ="primary")# primary means self adjusting acc to users theme 


# MAIN LOGIC
if generate_button:
    if not uploaded_files:
        st.warning("Please upload atleast one image.")
    elif len(uploaded_files) < 1 or len (uploaded_files) >10: # limiting number of images
        st.warning("Please upload maximun 5-10 images.")
    else:
        with st.spinner("The AI is writing and generating the story..(please wait)"):
            try:
                pil_images= [Image.open(uploaded_file) for uploaded_file in uploaded_files]
                st.subheader("Your visual Inspiration btw:")
                num_cols = min(4, len(pil_images))
                image_columns = st.columns(num_cols)

                for i, image in enumerate(pil_images):
                        with image_columns[i % num_cols]:
                          st.image(image, use_container_width=True)
                
                generate_story = generate_story_from_images(pil_images,story_style) # calling function from stry_gen.py
                if "Error" in generate_story or "failed" in generate_story or "API Key" in generate_story:
                    st.error(generate_story)
                else:
                    st.subheader(f"Your {story_style} style: ")
                    st.success(generate_story)

                st.subheader("Listen to your story") # narrating the story
                st.caption("Suggested playback speed: 1.5x")
                with st.spinner("Generating narration... please wait"):
                  audio_file = narrate_story(generate_story)
                  if audio_file:
                    st.audio(audio_file, format="audio/mp3")

            except Exception as e:
                st.error(f"An application error occured {e}")           
