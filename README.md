# Gemini Image Storyteller 🎨📖

This is an AI-powered Streamlit application that generates a creative story and narrated audio from uploaded images.
The idea behind this project was to explore **multimodal AI** — combining vision, language, and speech into a single interactive application.

Users can upload multiple images, choose a story style, and let the AI understand the visual context to create a story and narrate it.

 
 # Features
* Upload **1 to 10 images**
* Choose a story style (Comedy, Thriller, etc.)
* AI-generated story based on visual context
* Automatic **text-to-speech narration**
* Clean and responsive Streamlit UI
* User-friendly feedback using spinners, success, and error messages
* Deployed and publicly accessible via Streamlit Community Cloud

##  Live Demo

 **[https://gemini-image-storyteller-psiba.streamlit.app](https://gemini-image-storyteller-psiba.streamlit.app)**


##  Tech Stack
* **Python**
* **Streamlit** (UI & deployment)
* **Google Gemini API** (multimodal image-to-text)
* **PIL (Pillow)** for image processing
* **Text-to-Speech** for narration


##  How It Works :
1. User uploads one or more images
2. Images are processed and passed to the Gemini multimodal model
3. The model generates a story based on the selected style
4. The generated story is converted into audio narration
5. The story text and audio are displayed in the app


##  What I Learned
Building this project helped me gain **hands-on experience** with both AI and application development.
Some key learnings from this project include:
* Understanding and working with **multimodal AI models** that take images as input and generate text
* Using the **Google Gemini API** for image-to-text generation
* Designing a clean and user-friendly **Streamlit UI**
* Handling multiple image uploads and displaying them responsively using Streamlit columns
* Improving user experience with **spinners, captions, and status messages**
* Structuring a Python project by separating UI logic and AI logic
* Debugging layout and rendering issues related to Streamlit components
* Deploying a real-world application on **Streamlit Community Cloud**
* Writing clearer, more maintainable Python code
This project especially helped me move from just “writing code” to **thinking in terms of user experience and code flow**.

## Improvements that I might exectue in future:
* Add voice selection options for narration
* Allow users to control story length
* Support multiple languages
