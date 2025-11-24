import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel

from tools import read_user_profile, update_user_profile

load_dotenv()

# Initialize the Gemini client
gemini_client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY"),
)

# Initialize the OpenAIChatCompletionsModel adapted for Gemini
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=gemini_client,
)

# Configure the Agent
chatbot_agent = Agent(
    name="Personal Chatbot",
    instructions=(
        "You are a personal chatbot. Greet users by name if known. "
        "Detect when users share personal information (like their name or preferences) "
        "and save it using the provided tools. "
        "Use the read_user_profile tool to check for known information."
    ),
    tools=[read_user_profile, update_user_profile],
    model=gemini_model,
)
