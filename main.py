import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

# Import your custom agents
from career_agents.career_agent import CareerAgent

# chainlit ui event: Chat start
@cl.on_chat_start
async def chat_start():
    await cl.Message(content="👋 Hi! I'm your Career Mentor. What subjects are you interested in?").send()

# CLI event: On user message
@cl.on_message
async def main(msg: cl.Message):
    result = await Runner.run(CareerAgent, input=msg.content)
    await cl.Message(content=result.final_output).send()
