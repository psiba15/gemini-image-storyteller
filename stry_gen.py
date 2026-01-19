from dotenv import load_dotenv
load_dotenv()
import os
from google import genai
from gtts import gTTS
from io import BytesIO

api_key= os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found")

client= genai.Client(api_key=api_key)#obj to pass api key


def create_genz_prompt(style):
    base_prompt = f"""
**Your Persona:** You are a Gen-Z storyteller — expressive, funny, emotionally aware, and internet-savvy.
Your stories feel like viral reels, late-night thoughts, and Pinterest aesthetics.

**Your Goal:** Create ONE engaging story that connects all provided images in order.

**Style Requirement:** The story must fit the '{style}' genre.

**Core Rules:**
1. One continuous story with beginning, middle, and end.
2. Every image must influence the story.
3. Modern, Gen-Z friendly English (light slang allowed, no cringe).
4. Emotion-driven storytelling.

**Story Format:**
- Title: short & aesthetic.
- Length: 3–5 short paragraphs.
- Flow: binge-read friendly.
"""

    style_instruction = ""

    if style == "Comedy":
        style_instruction = """
**After the story, MUST add:**

[WHY THIS WAS FUNNY 🤡]:
Explain the chaos in one short paragraph.
"""

    elif style == "Thriller":
        style_instruction = """
**After the story, MUST add:**

[HEART RATE 📈]:
Describe the most intense scene.

[RED FLAG 🚩]:
The warning sign everyone ignored.

[LAST LINE ⚠️]:
End with one chilling sentence.
"""

    elif style == "Fairytale":
        style_instruction = """
**After the story, MUST add:**

[MAGIC ELEMENT ✨]:
Describe the magical or unreal aspect.

[FAIRYTALE MORAL 🌱]:
One simple life lesson.
"""

    elif style == "Sci-Fi":
        style_instruction = """
**After the story, MUST add:**

[FUTURE TECH 🤖]:
The advanced technology involved.

[WHAT WENT WRONG ⚙️]:
The flaw humans didn’t expect.

[FINAL THOUGHT 🌌]:
One deep line about the future.
"""

    elif style == "Mystery":
        style_instruction = """
**After the story, MUST add:**

[WHAT FELT OFF 👀]:
The first suspicious detail.

[THE CLICK 🧠]:
The moment everything made sense.

[SOLUTION 🔍]:
Reveal the culprit and key clue.
"""

    elif style == "Adventure":
        style_instruction = """
**After the story, MUST add:**

[THE QUEST 🗺️]:
What the characters were searching for.

[TURNING POINT ⛰️]:
The hardest challenge faced.

[ENDING VIBE 🌄]:
Describe the ending mood in one line.
"""

    elif style == "Morale":
        style_instruction = """
**After the story, MUST add:**

[LIFE LESSON 📖]:
A clear moral in one sentence.

[WHY IT MATTERS 💭]:
How this lesson applies to real life.
"""

    elif style == "sarcastic brainrot":
        style_instruction = """
**After the story, MUST add:**

[INTERNAL MONOLOGUE 😵]:
Overthinking in one messy paragraph.

[REALITY CHECK 💀]:
One brutally honest line.
"""

    elif style == "romance":
        style_instruction = """
**After the story, MUST add:**

[FEELINGS UNEXPRESSED 🫀]:
Emotional state of the main character.

[Moments ✨]:
A soft or heartbreaking moment.

[ENDING VIBE 🌙]:
One-word ending + short line.
"""

    return base_prompt + style_instruction




response= client.models.generate_content(
    model="gemini-2.5-flash",
    contents="What is asthetic explain in 10 words"
)
# print(response.text)

#writing a fuc that will accpect our files and styles and in return it'll generate story
def generate_story_from_images(images, style):
    response= client.models.generate_content(
         model="gemini-2.5-flash",
         contents=[images,create_genz_prompt(style)]
    )
    return response.text


# func that will take stories as an input and give audio file of the story
def narrate_story(story_text):
    try:
        tts = gTTS(text=story_text, lang="en", slow=False)
        audio_fp= BytesIO()#temp file
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)# if story regenerated the audio will satrt form begining
        return audio_fp
    except Exception as e:
        return f"An unexpected error occured during the API call."
    