import os 
from dotenv import load_dotenv
load_dotenv()

#encoding image 
import base64
def encode_image(image_path):
    image_file= open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

#LLM setup
from groq import Groq
def analyze_image_with_query(query,model,encoded_img):
    client = Groq(
        api_key=os.environ.get("groq_api")   
    )
    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type":"text",
                        "text":query
                    },
                    {
                        "type":"image_url",
                        "image_url":{"url":f"data:image/png;base64,{encoded_img}",
                        },
                    },
                ],
            }]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )
    return chat_completion.choices[0].message.content