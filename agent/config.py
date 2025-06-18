import yaml
from dotenv import load_dotenv

load_dotenv()

with open("../env.yaml", "r") as file:
    env = yaml.safe_load(file)

HUGGINGFACE_TOKEN = env["huggingface"]["api_token"]

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.1"
MODEL_KWARGS = {
    "temperature": 0.5,
    "max_new_tokens": 300
}