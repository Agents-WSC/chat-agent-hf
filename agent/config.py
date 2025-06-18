import yaml

with open("env.yaml", "r") as f:
    config = yaml.safe_load(f)

HUGGINGFACE_TOKEN = config["huggingface"]["api_token"]

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.1"
MODEL_KWARGS = {
    "temperature": 0.5,
    "max_new_tokens": 300
}