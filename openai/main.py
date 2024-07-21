from openai import OpenAI
import base64
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI()


def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')
  
image_path = "./debug/inputs/vscode.png"

# Getting the base64 string
base64_image = encode_image(image_path)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user", 
      "content": [
        {
          "type": "text",
          "text": "What’s in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/png;base64,{base64_image}"
          },
        },
      ]
       
    }
  ],
  
)

print(completion.choices[0])