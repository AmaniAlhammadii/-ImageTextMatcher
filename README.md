# ImageTextMatcher

## Purpose
The ImageTextMatcher project is an application that allows users to match images with corresponding texts. It enables users to upload their images and associated texts, classify the match, and convert texts to audio. The project utilizes a combination of Hugging Face models, the OpenAI GPT-3.5-turbo API, and Gradio to provide a seamless and interactive user interface.

## Main Files and Their Functions

- **ImageTextMatcher-Application.ipynb**: Contains all the key functionalities:
  - **Image-Text Matching**: Uses the `Salesforce/blip-itm-base-coco` model from Hugging Face to match images with texts.
  - **Text to Audio Conversion**: Utilizes the `gTTS` library to convert texts into audio files.
  - **Audio to Text Conversion**: Uses the `SpeechRecognition` library to convert audio files into texts.
  - **Gradio Interface**: Provides an easy-to-use interface for users to upload images, input texts, and upload audio files, then displays the match result and a motivational message.

- **ImageTextMatcher-Pipeline.ipynb**: Focuses on Hugging Face pipelines and the OpenAI API, including data storage and analysis.

- **ImageTextMatcher-Gradio.ipynb**: Emphasizes the Gradio components while also involving data storage and analysis.

## Hugging Face Pipelines
This project utilizes the following Hugging Face pipelines:

- **Image-Text Matching**: The `BlipForImageTextRetrieval` pipeline is used for matching images with texts.
- **Text to Speech**: The project uses `gTTS` for converting texts to audio.

## Instructions to Run the Code
### Prerequisites
Make sure to install the required libraries:
- Gradio
- gtts
- torch
- transformers
- SpeechRecognition
- Pillow

### Setting Up OpenAI API Key
Ensure you set up your API key in the `.env` file if you're using the OpenAI API.

### Running the Application
Execute the Python script. The Gradio interface will automatically launch in your browser.

### Using the Application
1. Upload an image.
2. Enter the corresponding text.
3. Optionally upload an audio file.
4. The application will display the match result and a motivational message.

## Expected Output from Gradio Interface
- **Inputs**:
  - Image: e.g., "image.jpg"
  - Text: e.g., "This text corresponds to the image."
  - Audio: optional audio file.

- **Outputs**:
  - Match Classification: e.g., "Match found" or "No match."
  - Message: e.g., "This image was great!"

## Links
- [[Hugging Face]([https://colab.research.google.com/drive/1UnAr6mH05vQ8GiB8uQTbBep4_r6gh2Kh?authuser=0#scrollTo=GWfR6jw8ZV4k](https://huggingface.co/spaces/amaniM/ImageTextMatcher))](#)
- [[Colab](https://colab.research.google.com/drive/1UnAr6mH05vQ8GiB8uQTbBep4_r6gh2Kh?authuser=0#scrollTo=GWfR6jw8ZV4k)](#)


## Authors
- [Amani Alhammadi]
- [Lamar Hisham]
