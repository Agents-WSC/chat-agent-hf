import os
from dotenv import load_dotenv

load_dotenv()

HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.1"
MODEL_KWARGS = {
    "temperature": 0.5,
    "max_new_tokens": 300
}