import chainlit as cl
from agents import Runner
from agent import chatbot_agent
from tools import read_user_profile, update_user_profile # Import for debugging/verification

@cl.on_chat_start
async def start():
    """
    Initializes the chatbot when a new chat session starts.
    Sends a static welcome message.
    """
    await cl.Message(content="Hello, how can I assist you today?").send()

@cl.on_message
async def main(message: cl.Message):
    """
    Handles incoming user messages, passes them to the agent,
    and sends the agent's response back to the UI.
    """
    # Create a Runner instance for the agent
    runner = Runner(starting_agent=chatbot_agent)

    # Run the agent with the user's message
    result = await runner.run(message.content)

    # Send the final text output to the UI
    await cl.Message(content=result.final_output).send()

    # Debug: Print tool outputs for verification
    print("\n--- Tool Outputs ---")
    for item in result.new_items:
        if item.type == "tool_end":
            print(f"Tool: {item.tool.name}, Output: {item.output}")
    print("--------------------")
