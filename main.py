import gradio as gr
from transformers import BlipForImageTextRetrieval, AutoProcessor
from gtts import gTTS
import speech_recognition as sr
import torch
from PIL import Image

# تحميل النماذج والمعالجات
image_model = BlipForImageTextRetrieval.from_pretrained("Salesforce/blip-itm-base-coco")
image_processor = AutoProcessor.from_pretrained("Salesforce/blip-itm-base-coco")

# دالة مطابقة الصورة مع النص
def image_text_matching(img, text):
    raw_image = img.convert('RGB')
    inputs = image_processor(images=raw_image, text=text, return_tensors="pt")
    outputs = image_model(**inputs)
    result = outputs[0][0]
    softmax_result = torch.softmax(result, dim=0)
    max_index = torch.argmax(softmax_result).item()
    return 'Match' if max_index == 1 else 'No Match'

# دالة تحويل النص إلى صوت
def text_to_audio(text):
    tts = gTTS(text=text, lang='en')  # يمكنك تعديل اللغة للنصوص العربية
    audio_file = "output.mp3"
    tts.save(audio_file)
    return audio_file

# دالة تحويل الصوت إلى نص
def audio_to_text(audio):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language='ar')
    return text

# إعداد واجهة Gradio
iface = gr.Interface(
    fn=lambda img, text, audio: (
        image_text_matching(img, text),
        text_to_audio(text),
        audio_to_text(audio) if audio else "No audio uploaded"
    ),
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Enter Text"),
        gr.Audio(label="Upload Audio", type="filepath")
    ],
    outputs=["text", "audio", "text"],
    title="ImageTextMatcher: Image-Text Matching and Audio Tasks",
    description="Upload an image and enter text to see if they match. Also, convert text to audio and audio to text."
)

# تشغيل الواجهة
iface.launch()
