# career_agents/career_agent.py

from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the model
model = LitellmModel(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Define the career path agent
CareerAgent = Agent(
    name="Career Path Guide",
    instructions="""
You are an expert career advisor.

🎯 Your goal is to:
- Understand the user's chosen field of interest
- Break it down into learning stages (Beginner → Intermediate → Advanced)
- Recommend certifications, courses, books, or communities for that field
- Keep answers structured, encouraging, and specific

Give your response in bullet points and make it easy to follow.
""",
    model=model
)
