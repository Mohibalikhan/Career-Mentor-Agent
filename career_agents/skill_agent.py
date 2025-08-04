# career_agents/skill_agent.py

import os
from dotenv import load_dotenv
from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

# Load environment variables
load_dotenv()

# Model setup
model = LitellmModel(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Define the SkillAgent
SkillAgent = Agent(
    name="Skill Recommender",
    instructions="""
🛠️ You are a skill recommender bot.

Given a specific career field, your task is to:
- List core technical and soft skills required in that field
- Mention popular tools, frameworks, or languages relevant to the field
- Suggest how to build those skills (courses, platforms, practice tips)

Format your response with section headings and bullet points.
""",
    model=model
)
