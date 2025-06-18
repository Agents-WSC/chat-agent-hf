from langchain.llms import HuggingFaceHub
from langchain.agents import initialize_agent, load_tools
from agent.config import HUGGINGFACE_TOKEN, MODEL_ID, MODEL_KWARGS
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACE_TOKEN

def create_agent():
    llm = HuggingFaceHub(
        repo_id=MODEL_ID,
        model_kwargs=MODEL_KWARGS
    )
    tools = load_tools(["llm-math"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent="zero-shot-react-description", verbose=True
    )
    return agent