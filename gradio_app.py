#INTERFACE 

from brain import encode_image, analyze_image_with_query
from voice_patient import record_audio, transcribe_with_groq
from voice_doctor import text_to_speech_with_gtts
import gradio as gr
import os
from dotenv import load_dotenv
load_dotenv()

system_prompt = """You have to act as a professional doctor. This is for learning purposes. 
Analyze the provided image and describe any medical concerns concisely. 
If you find any issues, suggest possible causes and remedies in a polite, professional tone. 
Avoid preamble; answer as if speaking to a real patient in a maximum of two sentences."""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(audio_filepath, "whisper-large-v3", os.environ.get("groq_api"))
    
    if image_filepath:
        doctor_response = analyze_image_with_query(
            system_prompt + speech_to_text_output, "llama-3.2-11b-vision-preview", encode_image(image_filepath)
        )
    else:
        doctor_response = "No image provided for analysis."
    
    voice_of_doctor = text_to_speech_with_gtts(doctor_response, "final.mp3")
    return speech_to_text_output, doctor_response, voice_of_doctor

# Professional UI Design
with gr.Blocks(theme=gr.themes.Default()) as iface:
    gr.Markdown("""
    # 🏥 AI Doctor Assistant
    **Analyze medical images and get expert-like feedback in seconds.**
    
    Upload an image and record your symptoms, and our AI will analyze and respond like a professional doctor.
    """)
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="🎤 Record Your Symptoms")
            image_input = gr.Image(type="filepath", label="📷 Upload Medical Image")
            submit_button = gr.Button("🔍 Analyze")
        
        with gr.Column():
            text_output = gr.Textbox(label="📝 Transcribed Symptoms", interactive=False)
            doctor_response = gr.Textbox(label="💡 Doctor's Diagnosis", interactive=False)
            audio_output = gr.Audio(label="🔊 AI Doctor's Response", interactive=False)
    
    submit_button.click(process_inputs, inputs=[audio_input, image_input], outputs=[text_output, doctor_response, audio_output])

iface.launch(debug=True)


